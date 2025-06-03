from random import randint

def random_rgb(input):
    def rand_hex():
        x = randint(0, 255)
        return f"#{x}:02x"
    for i, j in enumerate(input):
        full_dict = {j: {w: rand_hex() for w in 'rgb'}}
    return full_dict


# predefined_dict = random_rgb(ascii_lowercase)