from widget_wrapper import *


class Draw_Text_Widget_Group():
    def __init__(self, apply_func, dict,
                 font_size_def=12, text='', fill_color_def='#ffffff',
                 dict_slug='draw_text'):

        self.apply_func = apply_func
        self.dict = dict
        self.dict_slug = dict_slug

        self.text_length_ipywidget = widgets.BoundedIntText(value=1,
                                                          min=1,
                                                          max=1000,
                                                   description='Length:',
                                                   disabled=False
                                                   )

        self.text_length_wrapper = Widget_Wrapper(self.text_length_ipywidget)


        self.font_size_ipywidget = widgets.BoundedIntText(value=font_size_def,
                                                          min=1,
                                                          max=1000,
                                                   description='Font Size:',
                                                   disabled=False
                                                   )

        self.font_size_wrapper = Widget_Wrapper(self.font_size_ipywidget)


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
                                          tooltip='Draw Text'
                                          )

        self.draw_button.on_click(self.eventhander)


        self.top_box = widgets.HBox([self.text_length_wrapper.get_widget(),
                                        self.font_size_wrapper.get_widget()
                                        ])

        self.bottom_box = widgets.HBox([self.color_wrapper.get_widget(),
                                        self.draw_button
                                        ])

        self.main_box = widgets.VBox([self.top_box,
                                      self.bottom_box
                                      ])


    def reset(self):
        self.text_length_wrapper.reset()
        self.font_size_wrapper.reset()
        self.color_wrapper.reset()


    def update_dict(self):
        color = self.color_wrapper.get_widget_val()
        length = self.text_length_wrapper.get_widget_val()
        size = self.font_size_wrapper.get_widget_val()
        draw = partial(draw_text, length=length, size=size, fill=color)
        self.dict[self.dict_slug] = draw


    def eventhander(self, obj):
        self.update_dict()
        self.apply_func()



















#
