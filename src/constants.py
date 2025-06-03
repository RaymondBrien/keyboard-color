from string import ascii_lowercase as chars
from typing import Dict

from src.quick_dict import random_rgb

ENUM_LETTERS : Dict[str, int] = {l: i for i, l in enumerate(chars, start=1)}
REFRESH_TIME : int = 1
RANDOM_DICT : Dict[str, Dict[str, str]] = random_rgb(chars)