import pytest

from src.constants import NOTE_NAMES
from src.tuner_audio.threading_helper import ProtectedList
from src.tuner_audio.audio_analyzer import AudioAnalyzer


@pytest.fixture
def queue():
    yield ProtectedList()

@pytest.fixture
def audio_analyzer(queue):
    yield AudioAnalyzer(queue)


def test_returns_note_name(mocker, audio_analyzer):
    with mocker.patch(
    )

def test_note_change_equals_color_change():
    ...

