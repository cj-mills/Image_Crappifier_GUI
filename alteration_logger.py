
from utils import *
from widget_wrapper import *


class Alteration_Logger():

    def __init__(self):

        # self.options = [alteration for alteration in alteration_sequence]

        self.options = ['']

        self.alteration_sequence_list = widgets.SelectMultiple(
            options=self.options,
            value=[''],
            rows=6,
            description='Alterations:',
            disabled=False
        )

        self.log_path_widget = widgets.Text(
            value='',
            placeholder='Enter save path',
            description='Save Path:',
            disabled=False
        )

        self.refresh_button_widget = widgets.Button(
            description='Refresh',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Refresh alteration list',
        )

        self.delete_button_widget = widgets.Button(
            description='Delete',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Delete alteration',
        )


        self.load_path_widget = widgets.Text(
            value='',
            placeholder='Enter log path',
            description='Load Path:',
            disabled=False
        )

        self.load_button_widget = widgets.Button(
            description='Load',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Load log file',
        )


        self.save_path_widget = widgets.Text(
            value='',
            placeholder='Enter save path',
            description='Save Path:',
            disabled=False
        )

        self.save_button_widget = widgets.Button(
            description='Save',
            disabled=False,
            button_style='', # 'success', 'info', 'warning', 'danger' or ''
            tooltip='Save log file',
        )

        self.list_buttons = widgets.VBox([self.refresh_button_widget, self.delete_button_widget])

        self.all_widgets = widgets.VBox([widgets.HBox([self.alteration_sequence_list, self.list_buttons]),
                                        widgets.HBox([self.save_path_widget, self.save_button_widget]),
                                        widgets.HBox([self.load_path_widget, self.load_button_widget])])

        


























#
