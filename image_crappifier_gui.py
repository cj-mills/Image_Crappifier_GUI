from IPython.display import display

from dataset_selector import Dataset_Selector
from alteration_builder import Alteration_Builder
from alteration_logger import Alteration_Logger
from dataset_creator import Dataset_Creator

from ipywidgets import Layout

from utils import *
from widget_wrapper import *


class Image_Crappifier_GUI():

    def __init__(self):

        self.dataset_selector = Dataset_Selector()

        

        self.dataset_selector.image_dataset_selector.load_img_list_btn.on_click(self.load_img_list)
        self.dataset_selector.dataset_downloader.load_img_list_btn.on_click(self.load_img_list_from_download)
        self.dataset_selector.video_file_selector.save_btn.on_click(self.save_video_frame_btn_eventhandler)
        self.dataset_selector.video_file_selector.load_img_list_btn.on_click(self.load_img_list_from_video)

        self.dataset_loaded = False
        self.img_folder_path = Path('.')
        self.alteration_logger = Alteration_Logger()
        self.alteration_logger.refresh_button_widget.on_click(self.refresh_log_btn_click)
        self.alteration_logger.save_button_widget.on_click(self.save_log_btn_click)
        self.alteration_logger.load_button_widget.on_click(self.load_log_btn_click)
        self.alteration_logger.delete_button_widget.on_click(self.delete_alteration_btn_click)


        self.dataset_creator = Dataset_Creator()
        self.dataset_creator.create_button_widget.on_click(self.create_dataset)

        title_widget = widgets.HTML('<h2>Image Alteration UI</h2>')
        
        children = [
            self.dataset_selector.all_widgets,
            widgets.HTML("<h1>Dataset not selected.</h1>"), 
            self.alteration_logger.all_widgets, 
            self.dataset_creator.all_widgets
        ]

        self.base_accordion = widgets.Accordion(children=children)
        self.base_accordion.set_title(0, 'Dataset Selector')
        self.base_accordion.set_title(1, 'Alteration Builder')
        self.base_accordion.set_title(2, 'Alteration Logger')
        self.base_accordion.set_title(3, 'Dataset Creator')

        self.base_widget = widgets.VBox([title_widget, self.base_accordion])
        display(self.base_widget)

    def init_alteration_builder(self, path):
        # self.alteration_builder = Alteration_Builder(self.dataset_selector.dir_selector.get_path())
        self.alteration_builder = Alteration_Builder(path)
        children = [child for child in self.base_accordion.children]
        children[1] = self.alteration_builder.all_widgets
        self.base_accordion.children = children
        self.dataset_loaded = True
        self.dataset_creator.dataset_size_widget.max = len(self.alteration_builder.image_list)
        self.dataset_creator.dataset_size_widget.value = len(self.alteration_builder.image_list)


    def save_video_frame_btn_eventhandler(self, obj):
        # print(f"Saving video frames to {self.dataset_selector.video_file_selector.save_path.value}")
        self.img_folder_path = self.dataset_selector.video_file_selector.save_path.value
        save_video_frames(self.dataset_selector.video_file_selector.file_path.value, 
                            self.img_folder_path, "jpg")

    def load_img_list(self, obj):
        self.img_folder_path = self.dataset_selector.image_dataset_selector.get_path()
        self.init_alteration_builder(self.img_folder_path)

    def load_img_list_from_download(self, obj):
        self.img_folder_path = self.dataset_selector.dataset_downloader.get_path()
        self.init_alteration_builder(self.img_folder_path)

    def load_img_list_from_video(self, obj):
        self.init_alteration_builder(self.dataset_selector.video_file_selector.save_path.value)

    def refresh_log_btn_click(self, obj):
        self.alteration_logger.alteration_sequence_list.options = [alteration for alteration in self.alteration_builder.augmentation_dict.keys()]

    def delete_alteration_btn_click(self, obj):
        for alteration in self.alteration_logger.alteration_sequence_list.value:
            self.alteration_builder.augmentation_dict.pop(alteration)
        self.alteration_builder.update_img_widget()
        self.refresh_log_btn_click(obj)

    def save_log_btn_click(self, obj):
        save_obj(self.alteration_builder.augmentation_dict, self.alteration_logger.save_path_widget.value)

    def load_log_btn_click(self, obj):
        self.alteration_builder.augmentation_dict = load_obj(self.alteration_logger.load_path_widget.value)
        self.alteration_builder.update_img_widget()

    def create_dataset(self, obj):
        if self.dataset_loaded is True and self.dataset_creator.dataset_path_widget.value != "":
            crappify_dataset(self.img_folder_path, 
            Path(self.dataset_creator.dataset_path_widget.value), self.alteration_builder.augmentation_dict,
            self.dataset_creator.dataset_size_widget.value)


























#
