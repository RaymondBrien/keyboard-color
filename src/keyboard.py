import time, os
from string import ascii_lowercase as char
from typing import Dict

# from helpers import *  # TODO move these to helper file

ENUM_LETTERS = {l: i for i, l in enumerate(char)}

# Helper functions
def within_range(lower, input, upper) -> bool:
    return lower <= input <= upper

def under_25(input) -> bool:
#    return True if 0 <= input <= 25 else False
    return within_range(0, input, 25)

def under_255(value):
    """Max rgb value is 255"""
    return within_range(0, value, 255)


class RGB:

    def __init__(self):  # TODO change to dictionary
        self.rgb = {'r': 0, 'g': 0, 'b': 0}

    def validate_input(self, input):
        """
        Validate under 25 and return 
        its numeric value from ENUM_LETTERS dict
        """
        try:
            input = input.lower()
            under_25(ENUM_LETTERS[input])
            return ENUM_LETTERS[input]
        except (KeyError, ValueError):
            msg = f'{input} not allowed, returning default: '
            if isinstance(input, str):
                i = 'l'
                print(msg, i)
                return i
            if isinstance(input, int):
                i = 10
                print(msg, 10)
                return 10



    def map_to_r(self, input) -> int:
        """Letter number, exagerated for effect"""

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
        input = self.validate_input(input)
        if input >= 21:
            return input * 12
        else:
            return input * 9


    def collect_rgb(self, input) -> Dict[str, int]:  # TODO change to return rgb dict
        """
        Returns:
            Dict[str, int]  #rgb
        """

        r = self.map_to_r(input)
        g = self.map_to_g(input)
        b = self.map_to_b(input)

        self.rgb = {'r': r, 'g': g, 'b': b}
        return self.rgb


def run(input):  # TODO move to main file
        color = RGB()
        dict = color.collect_rgb(input)
        print(dict)

        time.sleep(0.5)

        # if dict == dict:
        #     input == None

        return dict

# TODO move to main file
if __name__ == '__main__':
    while True:
        run(input())

