import sys
import os.path
import pytest
import random
from code_1 import main
from mock_input_tests import *

def check_if_file_exists():
    try:
        exists = os.path.exists("code_1.py")
        assert exists == True
    except:
        sys.exit()

def test_right_guess():
    check_if_file_exists()
    guess = random.randint(1, 6)
    set_keyboard_input([guess]) #Simulating a guess from the user
    main(guess)
    output = get_display_output()

    assert output == [
        "Enter your guess:",
        "Rolling the dice...",
        "The dice shows "+guess,
        "Hooray! Your guess ("+guess+") was right."
        ]

def test_wrong_guess():
    check_if_file_exists()
    guess = random.randint(1, 6)
    set_keyboard_input([guess]) #Simulating a guess from the user
    main(guess+1)
    output = get_display_output()

    assert output == [
        "Enter your guess:",
        "Rolling the dice...",
        "The dice shows "+guess,
        "Hooray! Your guess ("+guess+") was right."
        ]

