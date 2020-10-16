from widget_wrapper import *

class Noise_Widget_Group():
    def __init__(self, apply_func, dict, dict_slug, widget_func):

        self.apply_func = apply_func
        self.dict = dict
        self.dict_slug = dict_slug
        self.widget_func = widget_func
        self.noise_scale_def = 0
        self.per_channel_def = False

        self.noise_scale_ipywidget = widgets.IntSlider(value=self.noise_scale_def,
                                                  min=0,
                                                  max=50,
                                                  step=1,
                                                  description='Scale:',
                                                  disabled=False,
                                                  continuous_update=True,
                                                  orientation='horizontal',
                                                  readout=True,
                                                  readout_format='d'
                                                  )

        self.noise_scale_wrapper = Widget_Wrapper(self.noise_scale_ipywidget)

        self.per_channel_ipywidget = widgets.Checkbox(value=True,
                                                 description='Per Channel',
                                                 disabled=False
                                                 )

        self.per_channel_wrapper = Widget_Wrapper(self.per_channel_ipywidget)

        self.button = widgets.Button(description='Apply',
                                     disabled=False,
                                     button_style='',
                                     tooltip='Apply'
                                     )

        self.button.on_click(self.eventhander)

        self.main_box = widgets.HBox([self.noise_scale_wrapper.get_widget(),
                                      self.per_channel_wrapper.get_widget(),
                                      self.button])


    def reset(self):
        self.noise_scale_wrapper.reset()
        self.per_channel_wrapper.reset()


    def update_dict(self):
        noise_scale = self.noise_scale_wrapper.get_widget_val()
        per_channel = bool(self.per_channel_wrapper.get_widget_val())

        noise = self.widget_func(scale=noise_scale,
                        per_channel=per_channel
                        )

        self.dict[self.dict_slug] = partial(noise)


    def eventhander(self, obj):
        self.update_dict()
        self.apply_func()


class Poisson_Noise_Widget_Group(Noise_Widget_Group):
    def __init__(self, apply_func, dict, dict_slug, widget_func):
        super().__init__(apply_func, dict, dict_slug, widget_func)

    def update_dict(self):
        lam = self.noise_scale_wrapper.get_widget_val()
        per_channel = bool(self.per_channel_wrapper.get_widget_val())

        noise = self.widget_func(lam=lam,per_channel=per_channel)

        self.dict[self.dict_slug] = partial(noise)
