from string import ascii_lowercase as lc
from typing import Tuple


ENUM_LETTERS = {l: i for i, l in enumerate(lc)}

# show color

def validate_input(input):
    """
    Validate under 25 and return 
    its numeric value from ENUM_LETTERS dict
    """
    if not under_25(ENUM_LETTERS[input]) and input.lower() in enum_letters:
        raise ValueError('must be a letter')

    return ENUM_LETTERS[input]

def get_input(input):
    while True:
        return validate_input(input)

def under_25(input):
    return True if input <= 25 else False

def under_255(value):
    """Max rgb value is 255"""
    return True if value <= 255 else False
def map_to_r(input):
    """Letter number, exagerated for effect"""
    input = validate_input(input)
    r = int((input * 1000) % 255)
    if under_255(r):
        print("r is: ", r)
        return r

        # otherwise return default value
    else: 
        return 130

def map_to_g(input):
    input = (validate_input(input) ** 2)
    if under_255(input):
        print('g is ', input)
        return input
    else:
        val = (input // 2) - 255
        return val if under_255(val) else 155


        
def map_to_b(input) -> int:
    input = validate_input(input)
    if input >= 21:
        print('b is ', input * 12)
        return input * 12
    else:
        print('b is ', input * 9)
        return input * 9


def assemble_rgb(r, g, b) -> Tuple[int, int, int]:
    print("rgb = ", r, g, b)
    return (r, g, b)

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

# testing
input = 'l'
print('for given input: ', input)
color = RGB()
print(color.collect_rgb(input))
