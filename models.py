from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
import json

debug = True

author = "Ivan Apaza & Luis Fernando Leyva"


class Constants(BaseConstants):
    players_per_group = None
    num_rounds = 1
    instructions_template = 'Choices/InstruccionesB.html'
    instructions_button = 'Choices/Instructions_Button.html'
    contact_template = 'Choices/Contactenos.html'

    name_in_url = 'Cigarettes_experiment_4'  # name in webbrowser


    name_in_url = 'SECCIÓN_II'

    # Answers = loosies. this part allow us to count the number of times loosie's are chosen
    quiz_fields = dict(
        question_1_response=1,
        question_2_response=1,
        question_3_response=1,
        question_4_response=1,
        question_5_response=1,
        question_6_response=1,
        question_7_response=1,
        question_8_response=1,
        question_9_response=1,
        question_10_response=1,
        question_11_response=1,
        question_12_response=1,

    )

    # This constant summarizes all 3 options
    options = [[1, 'Sueltos'],
                  [2, 'Cajetilla'],
                  [0, 'No Fumar']]


class Subsession(BaseSubsession):
    def creating_session(self):
        from .pages import initial_page_sequence
        ini = [i.__name__ for i in initial_page_sequence]
        for p in self.get_players():
            pb = ini.copy()
            random.shuffle(pb)
            p.page_sequence = json.dumps(pb)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    """Variable for randomizing page sequence"""
    page_sequence = models.StringField()

    """Quiz"""
    def current_field(self):
        return 'choice_{}_p'.format(self.quiz_page_counter + 1)

    """Variables for tracking changes in prices"""
    price_loosie_x10 = models.IntegerField(initial=8)
    price_package = models.IntegerField(initial=15)
    package_chosen = models.IntegerField(initial=0)
    stop = models.IntegerField(initial=0)
    quiz_page_counter = models.IntegerField(initial=0)

    """Variables for choices"""

    """Choices"""
    choice_1_p = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                              choices=Constants.options)
    choice_2_p = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                              choices=Constants.options)
    choice_3_p = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                              choices=Constants.options)
    choice_4_p = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                              choices=Constants.options)
    choice_5_p = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                              choices=Constants.options)
    choice_6_p = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                              choices=Constants.options)
    choice_7_p = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                              choices=Constants.options)
    choice_8_p = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                              choices=Constants.options)
    choice_9_p = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                              choices=Constants.options)
    choice_10_p = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                              choices=Constants.options)
    choice_11_p = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                              choices=Constants.options)
    choice_12_p = models.IntegerField(verbose_name='', widget=widgets.RadioSelect,
                                              choices=Constants.options)

    """Treatments"""
    choice_1_l = models.StringField(
        choices=[['1', 'Sueltos'], ['2', 'Cajetillas'], ['0', 'No Consume']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )

    choice_2_l = models.StringField(
        choices=[['1', 'Sueltos'], ['2', 'Cajetillas'], ['0', 'No Consume']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )
    choice_3_l = models.StringField(
        choices=[['1', 'Sueltos'], ['2', 'Cajetillas'], ['0', 'No Consume']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )
    choice_4_l = models.StringField(
        choices=[['1', 'Sueltos'], ['2', 'Cajetillas'], ['0', 'No Consume']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )
    choice_5_l = models.StringField(
        choices=[['1', 'Sueltos'], ['2', 'Cajetillas'], ['0', 'No Consume']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )
    choice_6_l = models.StringField(
        choices=[['1', 'Sueltos'], ['2', 'Cajetillas'], ['0', 'No Consume']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )

    choice_1_s = models.StringField(
        choices=[['1', 'Sueltos'], ['2', 'Cajetillas'], ['0', 'No Consume']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )

    choice_2_s = models.StringField(
        choices=[['1', 'Sueltos'], ['2', 'Cajetillas'], ['0', 'No Consume']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )

    choice_3_s = models.StringField(
        choices=[['1', 'Sueltos'], ['2', 'Cajetillas'], ['0', 'No Consume']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )

    choice_4_s = models.StringField(
        choices=[['1', 'Sueltos'], ['2', 'Cajetillas'], ['0', 'No Consume']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )

    choice_5_s = models.StringField(
        choices=[['1', 'Sueltos'], ['2', 'Cajetillas'], ['0', 'No Consume']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )

    choice_6_s = models.StringField(
        choices=[['1', 'Sueltos'], ['2', 'Cajetillas'], ['0', 'No Consume']],
        doc="""This player's decision""",
        widget=widgets.RadioSelect,
    )