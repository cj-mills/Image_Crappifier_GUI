import ipywidgets as widgets

from functools import partial
from fastai.utils.mem import *
from utils import *
import queue
from ipywidgets import Layout

class Dataset_Downloader():
    def __init__(self):
        
        self.cwd = Path.cwd()
        self.url = None

        self.options = ['CALTECH_101', 
                        # 'Caltech-UCSD Birds',
                        'CIFAR10', 
                        'CIFAR100',
                        'COCO_SAMPLE',
                        'COCO_TINY',
                        'DOGS_VS_CATS',
                        'FOOD',
                        'IMAGENETTE',
                        'MNIST',
                        'MNIST_SAMPLE',
                        'MNIST_TINY',
                        # 'OXFORD-IIIT_PET',
                        'OXFORD_102_FLOWERS',
                        # 'PLANET_SAMPLE',
                        # 'PLANET_TINY',  
                        'STANFORD_CARS',
                        ]
        
        self.existing_datasets = widgets.Select(
            options=self.options,
            value=None,
            # description='Dataset:',
            disabled=False,
            layout=Layout(width='98%')
        )

        self.save_path = widgets.Text(
            value=None,
            placeholder='Enter path to save dataset',
            description='',
            disabled=False,
            layout=Layout(width='74%')
        )

        self.save_btn = widgets.Button(
            description='Save',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Select Path',
            layout=Layout(width="24%")
        )

        self.save_btn.on_click(self.save_btn_eventhandler)


        self.save_description = widgets.HTML('<h4>Save Path: </h4>',
            layout=Layout(width='20%'))

        self.load_img_list_btn = widgets.Button(
            description='Load Image List',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Click to update the image list',
            layout=Layout(width="98.5%")
        )

        self.all_widgets = widgets.VBox([self.existing_datasets,
                            self.save_description,
                            widgets.HBox([self.save_path, self.save_btn]),
                            self.load_img_list_btn])


    def get_path(self):
        # print(self.cwd)
        return self.cwd

    def save_btn_eventhandler(self, obj):

        dest = '.' if self.save_path.value == None else self.save_path.value

        selection = self.existing_datasets.value

        if selection == "CALTECH_101":
            self.url = URLs.CALTECH_101
        elif selection == "Caltech_UCSD_Birds":
            self.url = URLs.CUB_200_2011
        elif selection == "CIFAR10":
            self.url = URLs.CIFAR
        elif selection == "CIFAR100":
            self.url = URLs.CIFAR_100
        elif selection == "COCO_SAMPLE":
            self.url = URLs.COCO_SAMPLE
        elif selection == "COCO_TINY":
            self.url = URLs.COCO_TINY
        elif selection == "DOGS_VS_CATS":
            self.url = URLs.DOGS
        elif selection == "FOOD":
            self.url = URLs.FOOD
        elif selection == "IMAGENETTE":
            self.url = URLs.IMAGENETTE
        elif selection == "MNIST":
            self.url = URLs.MNIST
        elif selection == "MNIST_SAMPLE":
            self.url = URLs.MNIST_SAMPLE
        elif selection == "MNIST_TINY":
            self.url = URLs.MNIST_TINY
        elif selection == "OXFORD_IIIT_PET":
            self.url = URLs.PETS
        elif selection == "OXFORD_102_FLOWERS":
            self.url = URLs.FLOWERS
        elif selection == "PLANET_SAMPLE":
            self.url = URLs.PLANET_SAMPLE
        elif selection == "PLANET_TINY":
            self.url = URLs.PLANET_TINY
        elif selection == "STANFORD_CARS":
            self.url = URLs.CARS

        

        self.cwd = Path(dest)

        output = untar_data(url=self.url, dest=dest)

        if (selection == "CALTECH_101"):
            output = '101_ObjectCategories'


        self.cwd = self.cwd/output

        # print(output)
