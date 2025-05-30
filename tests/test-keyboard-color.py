import pytest
import string

from keyboard import RGB

@pytest.fixture(scope=module)
def color():
    return RGB()

@pytest.paramaterize('input', string.printable)
def test_input_types(input, color):
    """All letters should pass, all symbols should not"""

    print('input is: ', input)
    rgb = color.collect_rgb(input)
    print(rgb)

    assert isinstance(tuple[int, int, int], rgb)
    assert list(rgb) < [255, 255, 255]
