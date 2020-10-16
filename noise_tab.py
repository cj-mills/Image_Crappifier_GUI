from noise_widget_group import *

class Noise_Tab():

    def __init__(self, apply_func=None, dict=None):

        gaussian_group = Noise_Widget_Group(apply_func, dict,
                                                  'gauss_noise', gaussian_noise)
        laplace_group = Noise_Widget_Group(apply_func, dict,
                                                 'laplace_noise', laplace_noise)
        poisson_group = Poisson_Noise_Widget_Group(apply_func, dict,
                                                 'poisson_noise', poisson_noise)

        titles = ['Gaussian', 'Laplace', 'Poisson']

        self.widget_list = [gaussian_group, laplace_group, poisson_group]

        accordion_children = [widget.main_box for widget in self.widget_list]
        self.accordion = widgets.Accordion(children=accordion_children)

        for index, title in enumerate(titles):
            self.accordion.set_title(index, title)


    def reset(self):
        for widget in self.widget_list:
            widget.reset()
