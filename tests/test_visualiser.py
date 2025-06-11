import pytest
from src.constants import NOTE_NAMES
from src.keyboard import run


@pytest.mark.parametrize("note_name",
                         ["C#", "D"])
def test_note_returns_dict(note_name):
    value =  run(note_name)  # currently keyboard
    assert 'r' in value
    assert 'g' in value
    assert 'b' in value

    # check valid rgb
    for i in value.values():
        assert i <= 255