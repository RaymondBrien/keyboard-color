import pytest
from src.keyboard import RGB
from src.constants import ENUM_LETTERS

@pytest.fixture
def enum_letters():
    yield ENUM_LETTERS

@pytest.fixture
def rgb():
    yield RGB()

def test_rgb_init(rgb):
    """rgb dictionary of RGB class should have 0's for each value"""
    assert rgb.rgb['r'] == 0
    assert rgb.rgb['g'] == 0
    assert rgb.rgb['b'] == 0

@pytest.mark.parametrize("letter, expected", [
    ("g", 7),
    ("b", 2),
    ("a", 1),
    ("z", 26),
])
def test_enum_letters(enum_letters, letter, expected):
    """a=1, b=2 etc"""
    assert enum_letters[letter] == expected

@pytest.mark.parametrize("input, expected", [
    ("r", 18),
    ("R", 18),
    ("NonExistantKey", 10),
    ("~", 10),
])
def test_validate_input(rgb, input, expected):
    """
    test: letter, number, symbol
    test over and under 25
    test returns enum_letters
    """
    assert rgb.validate_input(input) == expected

@pytest.mark.parametrize("input", ["z", "a"])
def test_map_to_r_under_255(rgb, input):
    assert rgb.map_to_r(input) <= 255
    with pytest.raises(TypeError):
        assert rgb.map_to_r(1)

@pytest.mark.parametrize("input", ["z", "a"])
def test_map_to_g(rgb, input):
    assert rgb.map_to_g(input) <= 255

@pytest.mark.parametrize("input", ["z", "a"])
def test_map_to_b(rgb, input):
    assert rgb.map_to_b(input) <= 255
