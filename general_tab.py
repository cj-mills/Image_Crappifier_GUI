from widget_wrapper import *
from resize_group import Resize_Group

class General_Tab():

    def __init__(self, apply_func=None, dict=None):

        self.resize_group = Resize_Group(apply_func, dict)


        # Compression Interface
        compression_ipywidget = widgets.IntSlider(value=0,
                                                  min=0,
                                                  max=100,
                                                  step=1,
                                                  description='Percentage:',
                                                  disabled=False,
                                                  continuous_update=True,
                                                  orientation='horizontal',
                                                  readout=True,
                                                  readout_format='d'
                                                  )

        compression_wrapper = Value_Widget(apply_func,
                                                   dict,
                                                   'compression',
                                                   compress,
                                                   compression_ipywidget
                                                   )


        # Contrast Interface
        contrast_ipywidget = widgets.FloatSlider(value=1.00,
                                                  min=0.0,
                                                  max=20.0,
                                                  step=0.1,
                                                  description='Gamma:',
                                                  disabled=False,
                                                  continuous_update=True,
                                                  orientation='horizontal',
                                                  readout=True,
                                                  readout_format='.2f'
                                                  )

        contrast_wrapper = Value_Widget(apply_func,
                                                   dict,
                                                   'contrast',
                                                   gamma_contrast,
                                                   contrast_ipywidget
                                                   )


        # Crop Square Interface
        crop_square_ipywidget = widgets.ToggleButton(value=False,
                                                     description='Crop Square',
                                                     disabled=False,
                                                     button_style='',
                                                     )

        crop_square_wrapper = Toggle_Widget(apply_func,
                                                   dict,
                                                   'crop_square',
                                                   crop_square,
                                                   crop_square_ipywidget
                                                   )

        titles = ['Resize', 'Contrast', 'Compression', 'Crop Square']

        self.widget_list = [self.resize_group, contrast_wrapper, compression_wrapper,
                            crop_square_wrapper]

        # accordion_children = [widget.main_box for widget in self.widget_list]
        accordion_children = [self.resize_group.main_box,
                              contrast_wrapper.get_widget(),
                              compression_wrapper.get_widget(),
                              crop_square_wrapper.get_widget()]

        self.accordion = widgets.Accordion(children=accordion_children)

        for index, title in enumerate(titles):
            self.accordion.set_title(index, title)


    def reset(self):
        for widget in self.widget_list:
            widget.reset()


















#
