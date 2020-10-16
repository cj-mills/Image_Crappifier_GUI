from widget_wrapper import *

class MotionBlurWidgetGroup():
    def __init__(self, apply_func, dict, dict_slug, widget_func):
        self.apply_func = apply_func
        self.dict = dict
        self.dict_slug = 'motion_blur'
        self.widget_func = widget_func

        self.kernel_size_ipywidget = widgets.IntSlider(
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
        self.kernel_size_wrapper = Widget_Wrapper(self.kernel_size_ipywidget)

        self.angle_ipywidget = widgets.IntSlider(
            value=0,
            min=0,
            max=360,
            step=1,
            description='Angle:',
            disabled=False,
            continuous_update=True,
            orientation='horizontal',
            readout=True,
            readout_format='d'
        )
        self.angle_wrapper = Widget_Wrapper(self.angle_ipywidget)

        self.direction_ipywidget = widgets.FloatSlider(
            value=0.0,
            min=-1.0,
            max=1.0,
            step=0.1,
            description='Direction:',
            disabled=False,
            continuous_update=True,
            orientation='horizontal',
            readout=True,
            readout_format='.1f'
        )
        self.direction_wrapper = Widget_Wrapper(self.direction_ipywidget)

        self.button = widgets.Button(description='Apply',
                                     disabled=False,
                                     button_style='',
                                     tooltip='Apply'
                                     )

        self.button.on_click(self.eventhander)

        top = widgets.HBox([self.kernel_size_wrapper.get_widget(),
                             self.angle_wrapper.get_widget(),
                             self.button
                             ])

        bottom = widgets.HBox([self.direction_wrapper.get_widget()])

        self.main_box = widgets.VBox([top, bottom])


    def reset(self):
        self.kernel_size_wrapper.reset()
        self.angle_wrapper.reset()
        self.direction_wrapper.reset()


    def update_dict(self):
        kernel_size = self.kernel_size_wrapper.get_widget_val()
        angle = self.angle_wrapper.get_widget_val()
        direction = self.direction_wrapper.get_widget_val()

        blur = self.widget_func(kernel_size=kernel_size, angle=angle,
                       direction=direction)

        self.dict[self.dict_slug] = partial(blur)


    def eventhander(self, obj):
        self.update_dict()
        self.apply_func()








#
