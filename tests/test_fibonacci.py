import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fibonacci import fibonacci

def test_fibonacci_correcto():
    assert fibonacci(10) == 55

def test_fibonacci_limite():
    assert fibonacci(0) == 0

def test_fibonacci_error():
    with pytest.raises(ValueError):
        fibonacci(-5)