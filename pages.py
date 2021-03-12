import math
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player, Group
import json
from django.conf import settings
import string
import random
import time

debug = True
#########################################################################
"""Authors: Ivan Apaza & Luis Fernando Leyva"""
#########################################################################


"""First, we enunciate instructional pages"""

class prices_overview(Page):
    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True
    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

"""Then, we continue with our first questionnaire"""
class p_1(Page):
    _allow_custom_attributes = True
    form_model = 'player'

    def is_displayed(self):
        return self.player.price_loosie_x10 < 13.1 and self.player.price_package < 20.1 and self.player.stop < 1 and self.participant.vars['non_smoker'] != True

    def get_form_fields(self):
        return [self.player.current_field()]

    def error_message(self, values):
        player = self.player
        current_field = player.current_field()

        if values[current_field] == 2:
            player.package_chosen += 1

        if values[current_field] == 0:
            player.stop += 1

    def vars_for_template(self):
        player = self.player
        index = player.quiz_page_counter
        return {'participant_id': self.participant.label,
                'page_number': index + 1,
                'price_loosie': self.player.price_loosie_x10 / 10}

    def before_next_page(self):
        player = self.player
        player.quiz_page_counter += 1

        if player.package_chosen == 0:
            player.price_loosie_x10 += 1
        if player.package_chosen == 1:
            player.price_package += 1

        player.package_chosen = 0



class p_2(Page):
    _allow_custom_attributes = True
    form_model = 'player'

    def is_displayed(self):
        return self.player.price_loosie_x10 < 13.1 and self.player.price_package < 20.1 and self.player.stop < 1 and \
               self.participant.vars['non_smoker'] != True

    def get_form_fields(self):
        return [self.player.current_field()]

    def error_message(self, values):
        player = self.player
        current_field = player.current_field()

        if values[current_field] == 2:
            player.package_chosen += 1

        if values[current_field] == 0:
            player.stop += 1

    def vars_for_template(self):
        player = self.player
        index = player.quiz_page_counter
        return {'participant_id': self.participant.label,
                'page_number': index + 1,
                'price_loosie': self.player.price_loosie_x10 / 10}

    def before_next_page(self):
        player = self.player
        player.quiz_page_counter += 1

        if player.package_chosen == 0:
            player.price_loosie_x10 += 1
        if player.package_chosen == 1:
            player.price_package += 1

        player.package_chosen = 0



class p_3(Page):
    _allow_custom_attributes = True
    form_model = 'player'

    def is_displayed(self):
        return self.player.price_loosie_x10 < 13.1 and self.player.price_package < 20.1 and self.player.stop < 1 and \
               self.participant.vars['non_smoker'] != True

    def get_form_fields(self):
        return [self.player.current_field()]

    def error_message(self, values):
        player = self.player
        current_field = player.current_field()

        if values[current_field] == 2:
            player.package_chosen += 1

        if values[current_field] == 0:
            player.stop += 1

    def vars_for_template(self):
        player = self.player
        index = player.quiz_page_counter
        return {'participant_id': self.participant.label,
                'page_number': index + 1,
                'price_loosie': self.player.price_loosie_x10 / 10}

    def before_next_page(self):
        player = self.player
        player.quiz_page_counter += 1

        if player.package_chosen == 0:
            player.price_loosie_x10 += 1
        if player.package_chosen == 1:
            player.price_package += 1

        player.package_chosen = 0



class p_4(Page):
    _allow_custom_attributes = True
    form_model = 'player'

    def is_displayed(self):
        return self.player.price_loosie_x10 < 13.1 and self.player.price_package < 20.1 and self.player.stop < 1 and \
               self.participant.vars['non_smoker'] != True

    def get_form_fields(self):
        return [self.player.current_field()]

    def error_message(self, values):
        player = self.player
        current_field = player.current_field()

        if values[current_field] == 2:
            player.package_chosen += 1

        if values[current_field] == 0:
            player.stop += 1

    def vars_for_template(self):
        player = self.player
        index = player.quiz_page_counter
        return {'participant_id': self.participant.label,
                'page_number': index + 1,
                'price_loosie': self.player.price_loosie_x10 / 10}

    def before_next_page(self):
        player = self.player
        player.quiz_page_counter += 1

        if player.package_chosen == 0:
            player.price_loosie_x10 += 1
        if player.package_chosen == 1:
            player.price_package += 1

        player.package_chosen = 0



class p_5(Page):
    _allow_custom_attributes = True
    form_model = 'player'

    def is_displayed(self):
        return self.player.price_loosie_x10 < 13.1 and self.player.price_package < 20.1 and self.player.stop < 1 and \
               self.participant.vars['non_smoker'] != True

    def get_form_fields(self):
        return [self.player.current_field()]

    def error_message(self, values):
        player = self.player
        current_field = player.current_field()

        if values[current_field] == 2:
            player.package_chosen += 1

        if values[current_field] == 0:
            player.stop += 1

    def vars_for_template(self):
        player = self.player
        index = player.quiz_page_counter
        return {'participant_id': self.participant.label,
                'page_number': index + 1,
                'price_loosie': self.player.price_loosie_x10 / 10}

    def before_next_page(self):
        player = self.player
        player.quiz_page_counter += 1

        if player.package_chosen == 0:
            player.price_loosie_x10 += 1
        if player.package_chosen == 1:
            player.price_package += 1

        player.package_chosen = 0



class p_6(Page):
    _allow_custom_attributes = True
    form_model = 'player'

    def is_displayed(self):
        return self.player.price_loosie_x10 < 13.1 and self.player.price_package < 20.1 and self.player.stop < 1 and \
               self.participant.vars['non_smoker'] != True

    def get_form_fields(self):
        return [self.player.current_field()]

    def error_message(self, values):
        player = self.player
        current_field = player.current_field()

        if values[current_field] == 2:
            player.package_chosen += 1

        if values[current_field] == 0:
            player.stop += 1

    def vars_for_template(self):
        player = self.player
        index = player.quiz_page_counter
        return {'participant_id': self.participant.label,
                'page_number': index + 1,
                'price_loosie': self.player.price_loosie_x10 / 10}

    def before_next_page(self):
        player = self.player
        player.quiz_page_counter += 1

        if player.package_chosen == 0:
            player.price_loosie_x10 += 1
        if player.package_chosen == 1:
            player.price_package += 1

        player.package_chosen = 0



class p_7(Page):
    _allow_custom_attributes = True
    form_model = 'player'

    def is_displayed(self):
        return self.player.price_loosie_x10 < 13.1 and self.player.price_package < 20.1 and self.player.stop < 1 and \
               self.participant.vars['non_smoker'] != True

    def get_form_fields(self):
        return [self.player.current_field()]

    def error_message(self, values):
        player = self.player
        current_field = player.current_field()

        if values[current_field] == 2:
            player.package_chosen += 1

        if values[current_field] == 0:
            player.stop += 1

    def vars_for_template(self):
        player = self.player
        index = player.quiz_page_counter
        return {'participant_id': self.participant.label,
                'page_number': index + 1,
                'price_loosie': self.player.price_loosie_x10 / 10}

    def before_next_page(self):
        player = self.player
        player.quiz_page_counter += 1

        if player.package_chosen == 0:
            player.price_loosie_x10 += 1
        if player.package_chosen == 1:
            player.price_package += 1

        player.package_chosen = 0



class p_8(Page):
    _allow_custom_attributes = True
    form_model = 'player'

    def is_displayed(self):
        return self.player.price_loosie_x10 < 13.1 and self.player.price_package < 20.1 and self.player.stop < 1 and \
               self.participant.vars['non_smoker'] != True

    def get_form_fields(self):
        return [self.player.current_field()]

    def error_message(self, values):
        player = self.player
        current_field = player.current_field()

        if values[current_field] == 2:
            player.package_chosen += 1

        if values[current_field] == 0:
            player.stop += 1

    def vars_for_template(self):
        player = self.player
        index = player.quiz_page_counter
        return {'participant_id': self.participant.label,
                'page_number': index + 1,
                'price_loosie': self.player.price_loosie_x10 / 10}

    def before_next_page(self):
        player = self.player
        player.quiz_page_counter += 1

        if player.package_chosen == 0:
            player.price_loosie_x10 += 1
        if player.package_chosen == 1:
            player.price_package += 1

        player.package_chosen = 0



class p_9(Page):
    _allow_custom_attributes = True
    form_model = 'player'

    def is_displayed(self):
        return self.player.price_loosie_x10 < 13.1 and self.player.price_package < 20.1 and self.player.stop < 1 and \
               self.participant.vars['non_smoker'] != True

    def get_form_fields(self):
        return [self.player.current_field()]

    def error_message(self, values):
        player = self.player
        current_field = player.current_field()

        if values[current_field] == 2:
            player.package_chosen += 1

        if values[current_field] == 0:
            player.stop += 1

    def vars_for_template(self):
        player = self.player
        index = player.quiz_page_counter
        return {'participant_id': self.participant.label,
                'page_number': index + 1,
                'price_loosie': self.player.price_loosie_x10 / 10}

    def before_next_page(self):
        player = self.player
        player.quiz_page_counter += 1

        if player.package_chosen == 0:
            player.price_loosie_x10 += 1
        if player.package_chosen == 1:
            player.price_package += 1

        player.package_chosen = 0



class p_10(Page):
    _allow_custom_attributes = True
    form_model = 'player'

    def is_displayed(self):
        return self.player.price_loosie_x10 < 13.1 and self.player.price_package < 20.1 and self.player.stop < 1 and \
               self.participant.vars['non_smoker'] != True

    def get_form_fields(self):
        return [self.player.current_field()]

    def error_message(self, values):
        player = self.player
        current_field = player.current_field()

        if values[current_field] == 2:
            player.package_chosen += 1

        if values[current_field] == 0:
            player.stop += 1

    def vars_for_template(self):
        player = self.player
        index = player.quiz_page_counter
        return {'participant_id': self.participant.label,
                'page_number': index + 1,
                'price_loosie': self.player.price_loosie_x10 / 10}

    def before_next_page(self):
        player = self.player
        player.quiz_page_counter += 1

        if player.package_chosen == 0:
            player.price_loosie_x10 += 1
        if player.package_chosen == 1:
            player.price_package += 1

        player.package_chosen = 0



class p_11(Page):
    _allow_custom_attributes = True
    form_model = 'player'

    def is_displayed(self):
        return self.player.price_loosie_x10 < 13.1 and self.player.price_package < 20.1 and self.player.stop < 1 and \
               self.participant.vars['non_smoker'] != True

    def get_form_fields(self):
        return [self.player.current_field()]

    def error_message(self, values):
        player = self.player
        current_field = player.current_field()

        if values[current_field] == 2:
            player.package_chosen += 1

        if values[current_field] == 0:
            player.stop += 1

    def vars_for_template(self):
        player = self.player
        index = player.quiz_page_counter
        return {'participant_id': self.participant.label,
                'page_number': index + 1,
                'price_loosie': self.player.price_loosie_x10 / 10}

    def before_next_page(self):
        player = self.player
        player.quiz_page_counter += 1

        if player.package_chosen == 0:
            player.price_loosie_x10 += 1
        if player.package_chosen == 1:
            player.price_package += 1

        player.package_chosen = 0



class p_12(Page):
    _allow_custom_attributes = True
    form_model = 'player'

    def is_displayed(self):
        return self.player.price_loosie_x10 < 13.1 and self.player.price_package < 20.1 and self.player.stop < 1 and \
               self.participant.vars['non_smoker'] != True

    def get_form_fields(self):
        return [self.player.current_field()]

    def error_message(self, values):
        player = self.player
        current_field = player.current_field()

        if values[current_field] == 2:
            player.package_chosen += 1

        if values[current_field] == 0:
            player.stop += 1

    def vars_for_template(self):
        player = self.player
        index = player.quiz_page_counter
        return {'participant_id': self.participant.label,
                'page_number': index + 1,
                'price_loosie': self.player.price_loosie_x10 / 10}

    def before_next_page(self):
        player = self.player
        player.quiz_page_counter += 1

        if player.package_chosen == 0:
            player.price_loosie_x10 += 1
        if player.package_chosen == 1:
            player.price_package += 1

        player.package_chosen = 0

class treatments_overview(Page):
    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True

    def before_next_page(self):
        player = self.player
        if player.price_loosie_x10 == 14:
            player.price_loosie_x10 -= 1
        if player.price_package == 21:
            player.price_package -= 1
        if player.stop == 1:
            player.price_loosie_x10 -= 2
            player.price_package -= 1
    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

class L_1(Page):
    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True
    form_model = 'player'
    form_fields = ['choice_1_l']
    def vars_for_template(self):
        return {'price_loosie': self.player.price_loosie_x10 / 10}

class L_2(Page):
    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True
    form_model = 'player'
    form_fields = ['choice_2_l']
    def vars_for_template(self):
        return {'price_loosie': self.player.price_loosie_x10 / 10}

class L_3(Page):
    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True
    form_model = 'player'
    form_fields = ['choice_3_l']
    def vars_for_template(self):
        return {'price_loosie': self.player.price_loosie_x10 / 10}

class L_4(Page):
    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True
    form_model = 'player'
    form_fields = ['choice_4_l']
    def vars_for_template(self):
        return {'price_loosie': self.player.price_loosie_x10 / 10}

class L_5(Page):
    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True
    form_model = 'player'
    form_fields = ['choice_5_l']
    def vars_for_template(self):
        return {'price_loosie': self.player.price_loosie_x10 / 10}

class L_6(Page):
    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True
    form_model = 'player'
    form_fields = ['choice_6_l']
    def vars_for_template(self):
        return {'price_loosie': self.player.price_loosie_x10 / 10}

class S_1(Page):
    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True
    form_model = 'player'
    form_fields = ['choice_1_s']
    def vars_for_template(self):
        return {'price_loosie': self.player.price_loosie_x10 / 10}

class S_2(Page):
    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True
    form_model = 'player'
    form_fields = ['choice_2_s']
    def vars_for_template(self):
        return {'price_loosie': self.player.price_loosie_x10 / 10}

class S_3(Page):
    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True
    form_model = 'player'
    form_fields = ['choice_3_s']
    def vars_for_template(self):
        return {'price_loosie': self.player.price_loosie_x10 / 10}

class S_4(Page):
    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True
    form_model = 'player'
    form_fields = ['choice_4_s']
    def vars_for_template(self):
        return {'price_loosie': self.player.price_loosie_x10 / 10}

class S_5(Page):
    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True
    form_model = 'player'
    form_fields = ['choice_5_s']
    def vars_for_template(self):
        return {'price_loosie': self.player.price_loosie_x10 / 10}

class S_6(Page):
    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True
    form_model = 'player'
    form_fields = ['choice_6_s']
    def vars_for_template(self):
        return {'price_loosie': self.player.price_loosie_x10 / 10}


initial_page_sequence = [
    L_1,
    L_2,
    L_3,
    L_4,
    L_5,
    L_6,
    S_1,
    S_2,
    S_3,
    S_4,
    S_5,
    S_6,
]

# Add QuizPage as questions on your quiz
page_sequence = [
    prices_overview,
    p_1,
    p_2,
    p_3,
    p_4,
    p_5,
    p_6,
    p_7,
    p_8,
    p_9,
    p_10,
    p_11,
    p_12,
    treatments_overview,
]

class L_0(Page):
    def inner_dispatch(self):
        page_seq = int(self.__class__.__name__.split('_')[1])
        page_to_show = json.loads(self.player.page_sequence)[page_seq]
        self._is_frozen = False
        self.__class__ = globals()[page_to_show]
        return super(globals()[page_to_show], self).inner_dispatch()

for i, _ in enumerate(initial_page_sequence):
    NewClassName = "Page_{}".format(i)
    A = type(NewClassName, (L_0,), {})
    locals()[NewClassName] = A
    page_sequence.append(locals()[NewClassName])


