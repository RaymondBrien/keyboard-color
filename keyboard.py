import subprocess, os, time
from pprint import pprint as pp
from string import ascii_lowercase as char
from typing import Tuple



ENUM_LETTERS = {l: i for i, l in enumerate(char)}

# show color

def validate_input(input):
    """
    Validate under 25 and return 
    its numeric value from ENUM_LETTERS dict
    """
    if not under_25(ENUM_LETTERS[input]):
        raise ValueError(f"Must be on of the following: \n {char}")

    return ENUM_LETTERS[input]

def get_input(input):
    while True:
        # time.wait  TODO update every 1 second
        return input

def within_range(lower, input, upper) -> bool:
    return lower <= input <= upper

def under_25(input) -> bool:
#    return True if 0 <= input <= 25 else False
    return within_range(0, input, 25)

def under_255(value):
    """Max rgb value is 255"""
    return within_range(0, value, 255)

def map_to_r(input):
    """Letter number, exagerated for effect"""
    input = validate_input(input)
    r = int((input * 1000) % 255)
    if under_255(r):
        return r

        # otherwise return default value
    else: 
        return 130

def map_to_g(input):
    input = (validate_input(input) ** 2)
    if under_255(input):
        return input
    else:
        val = (input // 2) - 255
        return val if under_255(val) else 155


        
def map_to_b(input) -> int:
    input = validate_input(input)
    if input >= 21:
        return input * 12
    else:
        return input * 9


class RGB:

    def __init__(self):

        self.r = 0
        self.g = 0
        self.b = 0

    def collect_rgb(self, input) -> Tuple[int, int, int]:
        """
        Collect r, g, b values from input
        using dedicated functions. 
        
        Returns:
            Tuple[int, int, int]  # rgb
        """

        self.r = map_to_r(input)
        self.g = map_to_g(input)
        self.b = map_to_b(input)

        return (self.r, self.g, self.b)

def run(input):
    while True:
    # testing  # TODO this will be replaced with test-keyboard file when imported with pytest
        color = RGB()
        tuple = color.collect_rgb(input)
        print(tuple)

        time.sleep(0.5)

        if tuple == tuple:
            break


if __name__ == '__main__':
    # subprocess.call()

    input = input()
    run(input)


