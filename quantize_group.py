from widget_wrapper import *

class Quantize_Group():
    def __init__(self, apply_func, dict, dict_slug, widget_func):

        self.apply_func = apply_func
        self.dict = dict
        self.dict_slug = dict_slug
        self.widget_func = widget_func
        self.min_colors = 2
        self.max_colors = 256

        self.quantize_ipywidget = widgets.BoundedIntText(value=self.max_colors,
                                               min=self.min_colors,
                                               max=self.max_colors,
                                               step=1,
                                               description='# of Colors:',
                                               disabled=False,
                                               continuous_update=False,
                                               orientation='horizontal',
                                               readout=True,
                                               readout_format='d'
                                               )

        self.quantize_wrapper = Widget_Wrapper(self.quantize_ipywidget)

        self.button = widgets.Button(description='Apply',
                                     disabled=False,
                                     button_style='',
                                     tooltip='Apply'
                                     )

        self.button.on_click(self.eventhander)

        self.main_box = widgets.HBox([self.quantize_wrapper.get_widget(),
                                      self.button])


    def reset(self):
        self.quantize_wrapper.reset()


    def update_dict(self):
        n_colors = self.quantize_wrapper.get_widget_val()
        self.dict[self.dict_slug] = partial(self.widget_func(n_colors))


    def eventhander(self, obj):
        self.update_dict()
        self.apply_func()
























#
