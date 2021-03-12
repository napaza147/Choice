from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from otree.api import SubmissionMustFail
from .models import Constants
import random as r


# FOR ALPHA/BETA TESTING
class PlayerBot(Bot): 
    """"This class represents a virtual player that will input the values that each page requires and that allows to
        test if there are errors in a specific page or field.

        -Yield statements will change the value of the fields
        -Assert statements check if the field values have a specific value or not
        -SubmissionMustFail stops the game if an invalid value submitted has been accepted
        
        There are two main modes for the bots

        *alpha: They check if the game runs with values that shouldn't be accepted by each variable. It checks:
            **inside the boundaries: checks for errors using inside the boundaries
            **in the boundaries: checks for errors using the boundary values (Because this task has fixed values
            predefined as answers, the fields should not accept this values unless the fixed answer is a bound. This is
            not the case for the Collateral Game task)
            **outside the boundaries: checks for errors using values outside the boundaries
            **different types of values: checks if the values that has been inputted are the same type of the respective
             variables

        *beta: They check how the game would run in a real environment with a big amount of players. To do this testing,
            its only needed to run a huge number of bots.
    """

    def play_round(self):

        yield (pages.QuizPage)
        yield (pages.QuizPage)
        yield (pages.QuizPage)
        yield (pages.QuizPage)
        yield (pages.QuizPage)
        yield (pages.QuizPage)
        yield (pages.QuizPage)
        yield (pages.QuizPage)
        yield (pages.QuizPage)
        yield (pages.QuizPage)
        yield (pages.QuizPage)
        yield (pages.QuizPage)
