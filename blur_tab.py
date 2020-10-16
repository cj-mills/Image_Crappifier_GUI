from widget_wrapper import *
from bilateral_blur_widget_group import BilateralBlurWidgetGroup
from motion_blur_widget_group import MotionBlurWidgetGroup

class Blur_Tab():

    def __init__(self, apply_func, dict):

        gaussian_blur_ipywidget = widgets.FloatSlider(value=0.0,
                                                   min=0.0,
                                                   max=10.0,
                                                   step=0.1,
                                                   description='Sigma Size:',
                                                   disabled=False,
                                                   continuous_update=True,
                                                   orientation='horizontal',
                                                   readout=True,
                                                   readout_format='.2f'
                                                   )

        gaussian_blur_wrapper = Value_Widget(apply_func, dict, 'gaussian_blur',
                                             gaussian_blur,
                                             gaussian_blur_ipywidget)

        gaussian_blur_widgets = widgets.HBox([gaussian_blur_wrapper.get_widget()])


        average_blur_ipywidget = widgets.IntSlider(
            value=0,
            min=0,
            max=20,
            step=1,
            description='Kernel Size:',
            disabled=False,
            continuous_update=True,
            orientation='horizontal',
            readout=True,
            readout_format='d'
        )

        average_blur_wrapper = Value_Widget(apply_func, dict, 'average_blur',
                                             average_blur,
                                             average_blur_ipywidget)

        average_blur_widgets = widgets.HBox([average_blur_wrapper.get_widget()])


        median_blur_ipywidget = widgets.IntSlider(
            value=3,
            min=3,
            max=30,
            step=2,
            description='Kernel Size:',
            disabled=False,
            continuous_update=True,
            orientation='horizontal',
            readout=True,
            readout_format='d'
        )

        median_blur_wrapper = Value_Widget(apply_func, dict, 'median_blur',
                                             median_blur,
                                             median_blur_ipywidget)

        median_blur_widgets = widgets.HBox([median_blur_wrapper.get_widget()])


        bilateral_group = BilateralBlurWidgetGroup(apply_func, dict,
                                                  'bilateral_blur', bilateral_blur)


        motion_group = MotionBlurWidgetGroup(apply_func, dict,
                                                  'motion_blur', motion_blur)


        titles = ['Gaussian', 'Average', 'Median', 'Bilateral', 'Motion']


        self.widget_list = [gaussian_blur_wrapper,
                            average_blur_wrapper,
                            median_blur_wrapper,
                            bilateral_group,
                            motion_group
                            ]

        # accordion_children = [widget.main_box for widget in self.widget_list]
        accordion_children = [gaussian_blur_widgets,
                                                average_blur_widgets,
                                                median_blur_widgets,
                                                bilateral_group.main_box,
                                                motion_group.main_box]
        self.accordion = widgets.Accordion(children=accordion_children)

        for index, title in enumerate(titles):
            self.accordion.set_title(index, title)


    def reset(self):
        for widget in self.widget_list:
            widget.reset()
