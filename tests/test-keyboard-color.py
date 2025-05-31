from Typing import Tuple
import pytest
import string

from keyboard import RGB

@pytest.fixture(scope=module)
def color():
    return RGB()

@pytest.fixture
def valid_rgb_tuple() -> Tuple[int, int, int]:
    return (50, 50, 50)

@pytest.fixture
@pytest.paramterize("_tuple", "('(50)', '(50, 50)', '(500, 50, 50)', '("a", "b", "c")'")
def bad_rgb_tuple() -> Tuple[Any]:
    return _tuple


def Display(rgb_tuple):
    """
    Display class requiers a valid rgb tuple.
    Mock displaying a validated rgb tuple 
    """
    valid = Tuple[int, int, int]
    if isinstance(rgb_tuple, valid):
        return True

    return False


# tests to write: 
    # check display falls back gracefully if invalid rgb
    # how does RGB class handle losing contact with display?
    # how does display handle different tuple feed regularities? eg every 0.5 seconds, every 0.1s, every minute, series of repeats, does that break?

# unit
@pytest.paramaterize('input', string.printable)
def test_input_types(input, color):
    """All letters should pass, all symbols should not"""

    print('input is: ', input)
    rgb = color.collect_rgb(input)
    print(rgb)

    assert isinstance(tuple[int, int, int], rgb)
    assert list(rgb) < [255, 255, 255]
