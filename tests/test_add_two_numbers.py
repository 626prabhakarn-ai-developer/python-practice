
import sys
from pathlib import Path

# Make project root importable when pytest runs from the tests/ folder
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest

from exercise.add_two_numbers import add


def test_add_integers():
    assert add("2", "3") == 5.0


def test_add_floats():
    assert add("1.5", "2.25") == 3.75


def test_add_negative_and_zero():
    assert add("-1", "1") == 0.0
    assert add("0", "0") == 0.0


def test_invalid_input_raises():
    with pytest.raises(ValueError):
        add("a", "3")
