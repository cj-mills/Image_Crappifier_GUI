from utils import *

class Widget_Wrapper():

    def __init__(self, widget):

        self.widget_val_def = widget.value
        self.widget_val = self.widget_val_def
        self.widget = widget

        self.widget.observe(self.eventhandler, names='value')


    def get_widget_val(self):
        return self.widget_val

    def get_widget(self):
        return self.widget


    def update_attr(self, new_val):
        self.widget_val = new_val


    def eventhandler(self, v):
        self.update_attr(v['new'])


    def reset(self):
        self.widget.unobserve(self.eventhandler, names='value')
        self.widget_val = self.widget_val_def
        self.widget.value = self.widget_val
        self.widget.observe(self.eventhandler, names='value')


class Augmentation_Widget(Widget_Wrapper):

    def __init__(self, apply_func, dict, dict_slug, widget_func, widget):
        super().__init__(widget)
        self.apply_func = apply_func
        self.widget_func = widget_func
        self.dict = dict
        self.dict_slug = dict_slug

    def apply_augmentation(self):
        self.apply_func()

    def update_dict(self):
        widget_val = self.widget_val
        self.dict[self.dict_slug] = partial(self.widget_func(widget_val))
        self.apply_augmentation()

    def update_attr(self, new_val):
        self.widget_val = new_val
        self.update_dict()

# @delegates
class Value_Widget(Augmentation_Widget):

    def __init__(self, apply_func, dict, dict_slug, widget_func, widget):
        super().__init__(apply_func, dict, dict_slug, widget_func, widget)

    def update_dict(self):

        widget_val = self.widget_val
        self.dict[self.dict_slug] = partial(self.widget_func(widget_val))
        self.apply_func()


class Toggle_Widget(Augmentation_Widget):

    def __init__(self, apply_func, dict, dict_slug, widget_func, widget):
        super().__init__(apply_func, dict, dict_slug, widget_func, widget)

    def update_dict(self):

        if self.widget_val is True:
            self.dict[self.dict_slug] = partial(self.widget_func)
        else:
            if self.dict_slug in self.dict:
                self.dict.pop(self.dict_slug)
        self.apply_func()



class Quantize_Widget(Augmentation_Widget):

    def __init__(self, apply_func, dict, dict_slug, widget_func, widget):
        super().__init__(apply_func, dict, dict_slug, widget_func, widget)

    def update_dict(self):

        n_colors = self.widget_val
        if n_colors <= 100:
            self.dict[self.dict_slug] = partial(self.widget_func(n_colors))
        else:
            if self.dict_slug in self.dict:
                self.dict.pop(self.dict_slug)
        self.apply_func()


class Image_Widget():

    def __init__(self, img):

        self.img_widget = widgets.Image(
            format='png',
        )
        self.update_img(img)


    def update_img(self, new_img) -> None:
        self.img_widget.value = pil_to_binary(new_img)







#
