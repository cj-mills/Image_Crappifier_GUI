
from dir_selector import Dir_Selector
from dataset_downloader import Dataset_Downloader
from file_selector import File_Selector

from utils import *
from widget_wrapper import *


class Dataset_Selector():

    def __init__(self):

        self.image_dataset_selector = Dir_Selector()
        self.dataset_downloader = Dataset_Downloader()
        self.video_file_selector = File_Selector()

        self.tab_nest = widgets.Tab()
        self.tab_nest.children = [self.image_dataset_selector.all_widgets, 
                                    self.dataset_downloader.all_widgets, 
                                    self.video_file_selector.all_widgets]
        self.tab_nest.set_title(0, 'Image Folder')
        self.tab_nest.set_title(1, 'Existing Dataset')
        self.tab_nest.set_title(2, 'Video File')

        self.all_widgets = widgets.VBox([self.tab_nest])
























#
