from typing import Dict
import tkinter as tk

# TODO move to hex
def dict_to_hex(rgb: Dict[str, int]) -> str:
    return f'#{rgb["r"]:02x}{rgb["g"]:02x}{rgb["b"]:02x}'

def update_color(canvas, rgb: Dict[str, int]) -> None:

    # setup
    color : str = dict_to_hex(rgb)
    canvas.config(bg=color)
    canvas.pack()