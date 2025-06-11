from string import ascii_lowercase as chars
from typing import Dict

from src.quick_dict import random_rgb

ENUM_LETTERS : Dict[str, int] = {l: i for i, l in enumerate(chars, start=1)}
REFRESH_TIME : int = 1
RANDOM_DICT : Dict[str, Dict[str, str]] = random_rgb(chars)

# live audio settings: (are tuned for best detecting string instruments like guitar)
SAMPLING_RATE = 48000  # mac hardware: 44100, 48000, 96000
CHUNK_SIZE = 1024  # number of samples
BUFFER_TIMES = 50  # buffer length = CHUNK_SIZE * BUFFER_TIMES
ZERO_PADDING = 3  # times the buffer length
NUM_HPS = 3  # Harmonic Product Spectrum

NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']