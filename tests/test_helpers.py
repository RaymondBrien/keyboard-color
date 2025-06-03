import pytest
import src.helpers as helpers

def test_within_range():
    """lower, input, upper -> bool"""
    assert helpers.within_range(0, 5, 10) == True
    assert helpers.within_range(0, 10, 10) == True
    assert helpers.within_range(0, 15, 10) == False
    with pytest.raises(TypeError):
        helpers.within_range(0, "a", 10)

def test_under_25():
    assert helpers.under_25(5) == True
    assert helpers.under_25(25) == True
    assert helpers.under_25(26) == False
    with pytest.raises(TypeError):
        helpers.under_25("a")

def test_under_255():
    assert helpers.under_255(5) == True
    assert helpers.under_255(255) == True
    assert helpers.under_255(256) == False
    with pytest.raises(TypeError):
        helpers.under_255("a")