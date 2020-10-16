from widget_wrapper import *
from quantize_group import Quantize_Group

class Color_Tab():

    def __init__(self, apply_func=None, dict=None):


        # Grayscale Interface
        grayscale_ipywidget = widgets.FloatSlider(value=0,
                                                  min=0,
                                                  max=1.0,
                                                  step=0.1,
                                                  description='Grayscale:',
                                                  disabled=False,
                                                  orientation='horizontal',
                                                  readout=True,
                                                  readout_format='.1f',
                                                  )

        grayscale_wrapper = Value_Widget(apply_func,
                                                 dict,
                                                 'grayscale',
                                                 grayscale,
                                                 grayscale_ipywidget
                                                 )


        kmeans_group = Quantize_Group(apply_func, dict,
                                                  'kmeans_quantize', kmeans_quantize)

        uniform_group = Quantize_Group(apply_func, dict,
                                                  'uniform_quantize', uniform_quantize)


        titles = ['Grayscale', 'Kmeans Quantize', 'Uniform Quantize']

        self.widget_list = [grayscale_wrapper, kmeans_group, uniform_group]

        # accordion_children = [widget.main_box for widget in self.widget_list]
        accordion_children = [grayscale_wrapper.get_widget(),
                              kmeans_group.main_box, uniform_group.main_box]
        self.accordion = widgets.Accordion(children=accordion_children)

        for index, title in enumerate(titles):
            self.accordion.set_title(index, title)


    def reset(self):
        for widget in self.widget_list:
            widget.reset()
























        #
