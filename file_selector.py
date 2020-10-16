import ipywidgets as widgets

from functools import partial
from fastai.utils.mem import *
import queue
from ipywidgets import Layout
from utils import save_video_frames

class File_Selector():
    def __init__(self, include_files=True):
        self.include_files = include_files
        self.cwd = Path.cwd()
        self.file_list = self.get_file_list()

        self.selector_widget = widgets.Select(
            options=self.file_list,
            value=None,
            disabled=False,
            layout=Layout(width='98%')
        )

        self.file_path = widgets.Text(
            value='',
            placeholder='Enter path to file',
            description='',
            disabled=False,
            layout=Layout(width='74%')
        )

        

        self.select_btn = widgets.Button(
            description='Select',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Select Path',
            layout=Layout(width="24%")
        )

        self.select_btn.on_click(self.select_btn_eventhander)


        self.save_path = widgets.Text(
            value='',
            placeholder='Enter path to save folder',
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


        self.select_description = widgets.HTML('<h4>Load Path: </h4>',
            layout=Layout(width='20%'))

        self.save_description = widgets.HTML('<h4>Save Path: </h4>',
            layout=Layout(width='20%'))

        self.selector_widget.observe(self.update_dirs, names='value')

        self.load_img_list_btn = widgets.Button(
            description='Load Image List',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Click to update the image list',
            layout=Layout(width="98.5%")
        )

        self.display_dir()

        self.all_widgets = widgets.VBox([self.selector_widget, self.select_description, 
        widgets.HBox([self.file_path, self.select_btn]),
        self.save_description,
        widgets.HBox([self.save_path, self.save_btn]),
        self.load_img_list_btn
        ])

    
    def get_file_list(self):
        file_list = [i.name for i in self.cwd.ls()]
        file_list.insert(0, '..')
        return file_list

    def get_path(self):
        return self.file_path.value

    def display_dir(self):
        if (Path(self.file_path.value).is_dir()):
            self.file_path.value = f"{self.cwd}"

    def update_dirs(self, change):

        self.selector_widget.unobserve(self.update_dirs, names='value')

        # print(Path(self.cwd/change['new']).is_dir())

        if change['new'] == '..':
            self.cwd = self.cwd.parent

            self.file_list = self.get_file_list()

            self.display_dir()

            self.selector_widget.options = self.file_list
            self.selector_widget.value = None

        elif Path(self.cwd/change['new']).is_dir():
            
            self.cwd = self.cwd/change['new']
            self.file_path.value = f"{self.cwd}"

            self.file_list = self.get_file_list()

            self.display_dir()

            self.selector_widget.options = self.file_list
            self.selector_widget.value = None

        else:
            self.file_path.value = f"{self.cwd/change['new']}"

        self.selector_widget.observe(self.update_dirs, names='value')

        

    def change_path(self, path):

        path = Path(path)
        value = None

        if not path.exists():
            return

        self.selector_widget.unobserve(self.update_dirs, names='value')

        if (path.is_dir()):
            pass
            
        elif (path.is_file()):
            path = path.parent
            value = Path(self.file_path.value).parts[-1]
        
        self.cwd = path
        
        self.file_list = self.get_file_list()

        self.display_dir()

        self.selector_widget.options = self.file_list
        self.selector_widget.value = value

        self.selector_widget.observe(self.update_dirs, names='value')

    def eventhander(self, obj):
        self.change_path(self.selector_widget.value)
    
    def select_btn_eventhander(self, obj):
        self.change_path(self.file_path.value)


        
