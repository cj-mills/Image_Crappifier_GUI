from widget_wrapper import *

class BilateralBlurWidgetGroup():
    def __init__(self, apply_func, dict, dict_slug, widget_func):
        self.apply_func = apply_func
        self.dict = dict
        self.dict_slug = 'bilateral_blur'
        self.widget_func = widget_func


        self.diameter_ipywidget = widgets.IntSlider(
            value=1,
            min=1,
            max=10,
            step=1,
            description='Diameter:',
            disabled=False,
            continuous_update=True,
            orientation='horizontal',
            readout=True,
            readout_format='d'
        )

        self.diameter_wrapper = Widget_Wrapper(self.diameter_ipywidget)

        self.sigma_color_ipywidget = widgets.IntSlider(
            value=10,
            min=10,
            max=250,
            step=5,
            description='σ Color:',
            disabled=False,
            continuous_update=True,
            orientation='horizontal',
            readout=True,
            readout_format='d'
        )

        self.sigma_color_wrapper = Widget_Wrapper(self.sigma_color_ipywidget)

        self.sigma_space_ipywidget = widgets.IntSlider(
            value=10,
            min=10,
            max=250,
            step=5,
            description='σ Space:',
            disabled=False,
            continuous_update=True,
            orientation='horizontal',
            readout=True,
            readout_format='d'
        )

        self.sigma_space_wrapper = Widget_Wrapper(self.sigma_space_ipywidget)

        self.button = widgets.Button(description='Apply',
                                     disabled=False,
                                     button_style='',
                                     tooltip='Apply'
                                     )

        self.button.on_click(self.eventhander)

        top = widgets.HBox([self.sigma_color_wrapper.get_widget(),
                             self.sigma_space_wrapper.get_widget(),
                             self.button
                             ])

        bottom = widgets.HBox([self.diameter_wrapper.get_widget()])

        self.main_box = widgets.VBox([top, bottom])


    def reset(self):
        self.diameter_wrapper.reset()
        self.sigma_color_wrapper.reset()
        self.sigma_space_wrapper.reset()


    def update_dict(self):
        diameter = self.diameter_wrapper.get_widget_val()
        sigma_color = self.sigma_color_wrapper.get_widget_val()
        sigma_space = self.sigma_space_wrapper.get_widget_val()

        blur = self.widget_func(diameter=diameter,
                       sigma_color=sigma_color,
                       sigma_space=sigma_space
                       )

        self.dict[self.dict_slug] = partial(blur)


    def eventhander(self, obj):
        self.update_dict()
        self.apply_func()
