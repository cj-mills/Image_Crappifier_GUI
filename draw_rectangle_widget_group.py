from widget_wrapper import *

class Draw_Rectangle_Widget_Group():
    def __init__(self, apply_func, dict, max_w_def=100, max_h_def=100,
                 fill_color_def='#ffffff',dict_slug='draw_rectangle'):

        self.apply_func = apply_func
        self.dict = dict
        self.dict_slug = dict_slug

        # Maximum Width Interface
        self.max_width_ipywidget = widgets.BoundedIntText(min=1,
                                                          max=1000,
                                                   value=max_w_def,
                                                   description='Max Width:',
                                                   disabled=False
                                                   )

        self.max_width_wrapper = Widget_Wrapper(self.max_width_ipywidget)

        # Maximum Height Interface
        self.max_height_ipywidget = widgets.BoundedIntText(min=1,
                                                           max=1000,
                                                    value=max_h_def,
                                                    description='Max Height:',
                                                    disabled=False
                                                    )

        self.max_height_wrapper = Widget_Wrapper(self.max_height_ipywidget)

        # Color Interface
        self.color_ipywidget = widgets.ColorPicker(concise=False,
                                                   description='Fill Color',
                                                   value=fill_color_def,
                                                   disabled=False
                                                   )

        self.color_wrapper = Widget_Wrapper(self.color_ipywidget)

        self.draw_button = widgets.Button(description='Draw',
                                          disabled=False,
                                          button_style='',
                                          tooltip='Draw Rectangle'
                                          )

        self.draw_button.on_click(self.eventhander)

        self.dimensions_box = widgets.HBox([self.max_width_wrapper.get_widget(),
                                        self.max_height_wrapper.get_widget()
                                        ])

        self.bottom_box = widgets.HBox([self.color_wrapper.get_widget(),
                                        self.draw_button
                                        ])

        self.main_box = widgets.VBox([self.dimensions_box,
                                      self.bottom_box
                                      ])


    def reset(self):
        self.color_wrapper.reset()
        self.max_width_wrapper.reset()
        self.max_height_wrapper.reset()


    def update_dict(self):
        color = self.color_wrapper.get_widget_val()
        max_w = self.max_width_wrapper.get_widget_val()
        max_h = self.max_height_wrapper.get_widget_val()

        draw = partial(draw_rectangle, color=color, max_w=max_w, max_h=max_h)
        self.dict[self.dict_slug] = draw


    def eventhander(self, obj):
        self.update_dict()
        self.apply_func()










#
