from draw_text_widget_group import Draw_Text_Widget_Group
from draw_rectangle_widget_group import Draw_Rectangle_Widget_Group
from draw_ellipse_widget_group import Draw_Ellipse_Widget_Group

import ipywidgets as widgets

class Draw_Tab():

    def __init__(self, apply_func, dict):

        self.text_group = Draw_Text_Widget_Group(apply_func, dict)
        self.rectangle_group = Draw_Rectangle_Widget_Group(apply_func, dict)
        self.ellipse_group = Draw_Ellipse_Widget_Group(apply_func, dict)
        titles = ['Text','Rectangle', 'Ellipse']

        self.widget_list = [self.text_group, self.rectangle_group,
                            self.ellipse_group]
        accordion_children = [widget.main_box for widget in self.widget_list]
        self.accordion = widgets.Accordion(children=accordion_children)

        for index, title in enumerate(titles):
            self.accordion.set_title(index, title)


    def reset(self):
        for widget in self.widget_list:
            widget.reset()




#
