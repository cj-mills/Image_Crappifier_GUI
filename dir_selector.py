import ipywidgets as widgets

from functools import partial
from fastai.utils.mem import *
import queue
from ipywidgets import Layout

class Dir_Selector():
    def __init__(self, include_files=False):
        self.include_files = include_files
        self.cwd = Path.cwd()
        self.dir_list = self.get_dir_list()

        self.selector_widget = widgets.Select(
            options=self.dir_list,
            value=None,
            disabled=False,
            layout=Layout(width='98%')
        )

        self.selected = widgets.Text(
            value='',
            placeholder='Enter path to dataset',
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

        self.select_btn.on_click(self.eventhander)


        self.description = widgets.HTML('<h4>Path: </h4>',
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

        self.all_widgets = widgets.VBox([self.selector_widget, self.description, 
        widgets.HBox([self.selected, self.select_btn]),
        self.load_img_list_btn
        ])

    
    def get_file_list(self):
        file_list = [i.name for i in self.cwd.ls()]
        file_list.insert(0, '..')
        return file_list

    def get_dir_list(self):
        dir_list = [i.name for i in self.cwd.ls() if i.is_dir()]
        dir_list.insert(0, '..')
        return dir_list

    def get_path(self):
        return self.selected.value

    def display_dir(self):
        self.selected.value = f"{self.cwd}"

    def update_dirs(self, change):

        self.selector_widget.unobserve(self.update_dirs, names='value')

        if change['new'] == '..':
            self.cwd = self.cwd.parent
        else:
            self.cwd = self.cwd/change['new']

        self.dir_list = self.get_dir_list()

        self.display_dir()

        self.selector_widget.options = self.dir_list
        self.selector_widget.value = None

        self.selector_widget.observe(self.update_dirs, names='value')

    def change_dirs(self, path):

        path = Path(path);

        if path.exists():
            self.cwd = path;
        else:
            return

        self.selector_widget.unobserve(self.update_dirs, names='value')

        self.dir_list = self.get_dir_list()

        self.display_dir()

        self.selector_widget.options = self.dir_list
        self.selector_widget.value = None

        self.selector_widget.observe(self.update_dirs, names='value')

    def eventhander(self, obj):
        self.change_dirs(self.selected.value)
