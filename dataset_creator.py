from utils import *
from widget_wrapper import *


class Dataset_Creator():

    def __init__(self):

        self.dataset_size_widget = widgets.BoundedIntText(
            value=1000,
            min=0,
            max=1000,
            step=1,
            description='Dataset Size:',
            disabled=False
        )

        self.dataset_path_widget = widgets.Text(
            value='',
            placeholder='Enter dataset path',
            description='Dataset Path:',
            disabled=False
        )
        self.create_button_widget = widgets.Button(
            description='Create',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Create a dataset at the specified path.',
        )

        self.all_widgets = widgets.VBox([self.dataset_size_widget, 
        widgets.HBox([self.dataset_path_widget, self.create_button_widget])])
























#
