
from general_tab import General_Tab
from color_tab import Color_Tab
from noise_tab import Noise_Tab
from blur_tab import Blur_Tab
from draw_tab import Draw_Tab

from collections import OrderedDict

from ipywidgets import Layout

from utils import *
from widget_wrapper import *


class Alteration_Builder():

    def __init__(self, dataset_path):

        self.init_alteration_builder(dataset_path)
        self.augmentation_dict = OrderedDict()

        self.general_tab = General_Tab(self.update_img_widget, self.augmentation_dict)
        self.color_tab = Color_Tab(self.update_img_widget, self.augmentation_dict)
        self.noise_tab = Noise_Tab(self.update_img_widget, self.augmentation_dict)
        self.blur_tab = Blur_Tab(self.update_img_widget, self.augmentation_dict)
        self.drawe_tab = Draw_Tab(self.update_img_widget, self.augmentation_dict)

        self.reset_btn = create_expanded_button('RESET', 'danger')
        self.previous_btn = create_expanded_button('PREVIOUS', '')
        self.next_btn = create_expanded_button('NEXT', '')

        self.reset_btn.on_click(self.reset_btn_eventhandler)
        self.previous_btn.on_click(self.previous_btn_eventhandler)
        self.next_btn.on_click(self.next_btn_eventhandler)

        self.tabs = widgets.Tab([self.general_tab.accordion,
                            self.color_tab.accordion,
                            self.noise_tab.accordion,
                            self.blur_tab.accordion,
                            self.drawe_tab.accordion])

        titles = ['General', 'Color', 'Noise', 'Blur', 'Draw']

        for index, title in enumerate(titles):
            self.tabs.set_title(index, title)

        control_widgets = widgets.AppLayout(header=None,
                                            left_sidebar=self.previous_btn,
                                            center=None,
                                            right_sidebar=self.next_btn,
                                            footer=self.reset_btn,
                                            height="120px",
                                            border='solid')


        image_display = widgets.VBox([self.img_widget.img_widget])
        image_display.layout.align_items = 'center'

        self.all_widgets = widgets.VBox([self.tabs, control_widgets, image_display])

    def init_alteration_builder(self, dataset_path):
        self.image_list = ImageList.from_folder(dataset_path).items
        self.il_index = 0;
        self.source_img = Image.open(self.image_list[self.il_index])
        self.img_widget = Image_Widget(self.source_img)

    def reset_dict(self):
        for key in list(self.augmentation_dict.keys()):
            self.augmentation_dict.pop(key)


    def reset_widgets(self) -> None:
        self.img_widget.update_img(self.source_img)
        self.reset_dict()

        self.general_tab.reset()
        self.color_tab.reset()
        self.noise_tab.reset()
        self.blur_tab.reset()
        self.drawe_tab.reset()


    def update_img_widget(self):
        new_img = apply_aug_dict(self.source_img, self.augmentation_dict)
        self.img_widget.update_img(new_img)


    def reset_btn_eventhandler(self, obj):
        self.reset_widgets()


    def increment_il_index(self):
        self.il_index += 1


    def decrement_il_index(self):
        self.il_index -= 1


    def get_next_img(self, update_index_func):
        if abs(self.il_index) == len(self.image_list) - 1:
            self.il_index = 0
        else:
            update_index_func()

        self.source_img = Image.open(self.image_list[self.il_index])
        self.update_img_widget()


    def previous_btn_eventhandler(self, obj):
        self.get_next_img(self.decrement_il_index)


    def next_btn_eventhandler(self, obj):
        self.get_next_img(self.increment_il_index)


























#
