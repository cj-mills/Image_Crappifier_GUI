from widget_wrapper import *

class Resize_Group():
    def __init__(self, apply_func, dict, dict_slug='resize', widget_func=resize):
        self.apply_func = apply_func
        self.dict = dict
        self.dict_slug = dict_slug
        self.widget_func = widget_func


        self.resize_ipywidget = widgets.BoundedIntText(value=540,
                                                 min=1,
                                                 max=2000,
                                                 description='Short Side:',
                                                 disabled=False
                                                 )

        self.resize_wrapper = Widget_Wrapper(self.resize_ipywidget)


        self.button = widgets.Button(description='Apply',
                                     disabled=False,
                                     button_style='',
                                     tooltip='Apply'
                                     )

        self.button.on_click(self.eventhander)


        self.main_box = widgets.HBox([self.resize_wrapper.get_widget(),
                                      self.button])


    def reset(self):
        self.resize_wrapper.reset()


    def update_dict(self):
        size = self.resize_wrapper.get_widget_val()
        self.dict[self.dict_slug] = partial(self.widget_func(min_size=size))


    def eventhander(self, obj):
        self.update_dict()
        self.apply_func()








#
