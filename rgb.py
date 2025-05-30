from typing import Tuple
from keyboard import map_to_r, map_to_g, map_to_b

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
