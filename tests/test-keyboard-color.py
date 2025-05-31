from typing import Dict, Any, Generator
import pytest
import string

from keyboard import RGB

@pytest.fixture
def color():
    yield RGB()

# @pytest.fixture
# def valid_rgb_dict() -> Generator[Dict[str, int], None, None]:
#     yield {'r': 50, 'g': 50, 'b': 50}

# # @pytest.fixture
# # @pytest.paramterize("_tuple", "('(50)', '(50, 50)', '(500, 50, 50)', '("a", "b", "c")'")
# # def bad_rgb_dict() -> Dict[str, int]:
# #     yield _tuple


# def Display(rgb_dict):
#     """
#     Display class requiers a valid rgb tuple.
#     Mock displaying a validated rgb tuple
#     """
#     if isinstance(rgb_dict, dict):
#         return True

#     return False



# unit
@pytest.mark.parametrize('input', string.ascii_letters)
def test_input_types(color, input):
    """All letters should pass, all symbols should not"""

    rgb = color.collect_rgb(input)
    assert isinstance(rgb, dict)
    assert list(rgb.values()) <= [255, 255, 255]
