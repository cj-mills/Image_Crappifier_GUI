import fastai
from fastai.vision import *
from fastai.callbacks import *
from fastai.utils.mem import *

from PIL import Image, ImageDraw, ImageOps, ImageEnhance, ImageFont
from functools import partial
from os import path
import numpy as np
import secrets
import os.path
import pickle
import string
import random
import io

import ffmpeg

import imageio
import imgaug as ia
from imgaug import augmenters as iaa

import ipywidgets as widgets



def save_video_frames(video_file_path, save_path, img_format="png"):
    Path(save_path).mkdir(parents=True, exist_ok=True)
    ffmpeg.input(video_file_path).output(f'{save_path}/%d.{img_format}').run();


def save_obj(obj, path):
    with open(path, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(path):
    with open(path, 'rb') as f:
        return pickle.load(f)


#
def save_dest(fn, path_lr, path_hr):
    dest = path_lr/fn.relative_to(path_hr)
    dest.parent.mkdir(parents=True, exist_ok=True)
    return dest


#
def save_img(img, dest_str: str, save_format:str='PNG', quality=100):
    save_f = save_format.upper()

    dest_str = remove_ext(dest_str)

    if save_f == 'PNG':
        img.save(dest_str+'png', 'PNG')
    elif save_f == 'JPEG':
        img.save(dest_str+'jpeg', 'JPEG', quality=quality)


def create_expanded_button(description, button_style):
    return widgets.Button(description=description, button_style=button_style,
                          layout=widgets.Layout(height='auto', width='auto')
                          )


def pil_to_binary(img):
    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format='PNG')
    return imgByteArr.getvalue()


#
def remove_ext(f_name: str, keep_dot: bool=True):
    return f_name[:f_name.rindex('.')+int(keep_dot)]


def to_imgaug(img):
    return imageio.core.util.Array(np.array(img))


def parse_aug_dict(aug_dict):
    imgaug_list = []
    pil_list = []

    for val in aug_dict.values():
        if 'imgaug' in str(type(val.func)):
            imgaug_list.append(val.func)
        else:
            pil_list.append(val)

    return imgaug_list, pil_list


def apply_imgaug(img, imgaug_list):
    seq = iaa.Sequential(imgaug_list)
    img = to_imgaug(img)
    images_aug = seq.augment_images([img])
    return Image.fromarray(images_aug[0].astype(np.uint8))


def apply_pil(img, pil_list):
    for aug in pil_list:
        img = aug(img)
    return img


def apply_aug_dict(img, aug_dict):
    imgaug_list, pil_list = parse_aug_dict(aug_dict)
    img = apply_imgaug(img, imgaug_list)
    img = apply_pil(img, pil_list)
    return img

def gamma_contrast(gamma):
    return iaa.GammaContrast(gamma)

def kmeans_quantize(n_colors):
    return  iaa.KMeansColorQuantization(n_colors=n_colors, max_size=None)


def uniform_quantize(n_colors):
    return  iaa.UniformColorQuantization(n_colors=n_colors, max_size=None)


def grayscale(alpha):
    return iaa.Grayscale(alpha=(alpha))


def compress(percentage):
    return  iaa.JpegCompression(compression=percentage)


def gaussian_blur(sigma):
    return iaa.blur.GaussianBlur(sigma=sigma)


def average_blur(kernel_size):
    return iaa.blur.AverageBlur(k=kernel_size)


def median_blur(kernel_size):
    return iaa.blur.MedianBlur(k=kernel_size)


def bilateral_blur(diameter, sigma_color, sigma_space):
    return iaa.blur.BilateralBlur(d=diameter, sigma_color=sigma_color,
                                  sigma_space=sigma_space)


def motion_blur(kernel_size, angle, direction):
    return iaa.blur.MotionBlur(k=kernel_size, angle=angle, direction=direction)


def gaussian_noise(scale, per_channel):
    return iaa.AdditiveGaussianNoise(scale=scale, per_channel=per_channel)


def laplace_noise(scale, per_channel):
    return iaa.AdditiveLaplaceNoise(scale=scale, per_channel=per_channel)


def poisson_noise(lam, per_channel):
    return iaa.AdditivePoissonNoise(lam=lam, per_channel=per_channel)


def min_size(img):
    return min(update_class.source_img.size)


def resize(min_size):
    resize_dict = {"shorter-side": min_size, 'longer-side': "keep-aspect-ratio"}
    return iaa.Resize(resize_dict)


# from https://github.com/fastai/fastai/blob/master/fastai/vision/data.py#L199
def resize_to(img, targ_sz:int, use_min:bool=False):
    "Size to resize to, to hit `targ_sz` at same aspect ratio, in PIL coords (i.e w*h)"
    w,h = img.size
    min_sz = (min if use_min else max)(w,h)
    ratio = targ_sz/min_sz
    return int(w*ratio),int(h*ratio)

#
def resize_pil(img, size=None, use_min=True):
    targ_sz = resize_to(img, size, use_min=use_min)
    return img.resize(targ_sz, resample=Image.BILINEAR).convert('RGB')


#
def change_contrast(img, factor: float=1.0):
    contrast = ImageEnhance.Contrast(img)
    return contrast.enhance(factor=factor)


#
def transpose_img(img, transpose_type: int):
    return img.transpose(transpose_type)


#
def square_padding(img):

    size = img.size  # img.size is in (width, height) format
    square_size = max(size)

    new_img = Image.new("RGB", (square_size, square_size))
    new_img.paste(img, ((square_size-size[0])//2,
                        (square_size-size[1])//2))

    return new_img


def crop_square(img):

    width, height = img.size   # Get dimensions
    min_dim = min(img.size)

    left = (width - min_dim)/2
    top = (height - min_dim)/2
    right = (width + min_dim)/2
    bottom = (height + min_dim)/2

    # Crop the center of the image
    return img.crop((left, top, right, bottom))


def generate_text(length, charset=string.printable):
    return ''.join(secrets.choice(charset) for i in range(length))


def draw_text(img, length, size, fill, font_file="./fonts/arial.ttf"):

    text = generate_text(length)

    font = ImageFont.truetype(font_file, size)

    draw = ImageDraw.Draw(img)
    offset=font.getsize(text)
    cx = random.randint(0, abs(img.size[0]-offset[0]))
    cy = random.randint(0, abs(img.size[1]-offset[1]))

    draw.text((cx, cy), text=text, font=font, fill=fill)
    return img


def draw_rectangle(img, color, max_w, max_h):

    draw = ImageDraw.Draw(img)

    width = random.randint(1, max_w)
    height = random.randint(1, max_h)

    cx = random.randint(0, abs(img.size[0]-width))
    cy = random.randint(0, abs(img.size[1]-height))

    draw.rectangle([(cx, cy), (cx+width,cy+height)], fill=color)
    return img


def draw_ellipse(img, color, max_w, max_h):

    draw = ImageDraw.Draw(img)

    width = random.randint(1, max_w)
    height = random.randint(1, max_h)

    cx = random.randint(0, abs(img.size[0]-width))
    cy = random.randint(0, abs(img.size[1]-height))

    draw.ellipse([(cx, cy), (cx+width,cy+height)], fill=color)
    return img

#
def crappify_img(fn, i, path_hr, path_lr, aug_dict, save_format='PNG', save_quality=(100)):
    img = Image.open(fn)
    img = apply_aug_dict(img, aug_dict)

    dest_str = str(save_dest(fn, path_lr, path_hr))
    save_img(img, dest_str, save_format, save_quality)





def crappify_dataset(path_hr, path_lr, aug_dict, dataset_size):
    il = ImageList.from_folder(path_hr).items

    if (dataset_size < len(il)):
        subset = random.sample(range(len(il) - 1), dataset_size)
        il = il[subset]

    if not path_lr.exists():
        print(f"Saving augmented images to {path_lr}")
        parallel(partial(crappify_img, path_lr=path_lr, path_hr=path_hr, aug_dict=aug_dict), il)
    else:
        print('Already Exists')


def delegates(to=None, keep=False):
    "Decorator: replace `**kwargs` in signature with params from `to`"
    def _f(f):
        if to is None: to_f,from_f = f.__base__.__init__,f.__init__
        else:          to_f,from_f = to,f
        sig = inspect.signature(from_f)
        sigd = dict(sig.parameters)
        k = sigd.pop('kwargs')
        s2 = {k:v for k,v in inspect.signature(to_f).parameters.items()
              if v.default != inspect.Parameter.empty and k not in sigd}
        sigd.update(s2)
        if keep: sigd['kwargs'] = k
        from_f.__signature__ = sig.replace(parameters=sigd.values())
        return f
    return _f


