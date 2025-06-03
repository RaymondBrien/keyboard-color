from random import randint
from string import ascii_letters, ascii_lowercase

def random_rgb(input):
    def rand_hex():
        x = randint(0, 255)
        return f"#{x}:02x"
    for i, j in enumerate(input):
        print({j: {w: rand_hex() for w in 'rgb'}})


predefined_dict = random_rgb(ascii_lowercase)