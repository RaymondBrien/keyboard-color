from typing import Dict
import time
from logging import log

from src.constants import ENUM_LETTERS, RANDOM_DICT
from src.helpers import *


class RGB:

    def __init__(self):  # TODO change to dictionary
        self.rgb = {'r': 0, 'g': 0, 'b': 0}

    def validate_input(self, input) -> int:
        """
        Validate under 25 and return 
        its numeric value from ENUM_LETTERS dict
        """
        if not isinstance(input, str):
            raise TypeError(f"Input must be type str.\n- {input} of type {type(input)} not allowed")
        try:
            input = input.lower()
            return ENUM_LETTERS[input]
        except (KeyError, ValueError):
            msg = f'{input} not in ENUM_LETTERS, returning default: '
            i = 10
            print(msg, i)
            return 10

    def map_to_r(self, input) -> int:
        """
        Args:
            input: str (must be letter of alphabet)
        Returns:
            int <= 250
        """
        input = self.validate_input(input)
        r = int((input * 1000) % 255)
        if under_255(r):
            return r
        else: 
            return 130

    def map_to_g(self, input) -> int:
        """Input squared"""
        input = (self.validate_input(input) ** 2)
        if under_255(input):
            return input
        else:
            val = (input // 2) - 255
            return val if under_255(val) else 155

    def map_to_b(self, input) -> int:
        """Input * 9"""
        input = self.validate_input(input)
        val = input * 9
        if under_255(val):
            return val
        else:
            log(level=1, msg=ValueError(f"Input ({input}) too high"))
            return 255

    def collect_rgb(self, input) -> Dict[str, int]:  # TODO change to return rgb dict
        """
        Based on single input, map its rgb value, save in memory.

        Returns:
            Dict[str, int]  #rgb
        """

        r = self.map_to_r(input)
        g = self.map_to_g(input)
        b = self.map_to_b(input)

        self.rgb = {'r': r, 'g': g, 'b': b}
        return self.rgb


def run(input):
        color = RGB()
        dict = color.collect_rgb(input)
        print(dict)

        return dict

def run_shorter(input):
    print(RANDOM_DICT)