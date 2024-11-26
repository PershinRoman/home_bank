from turtledemo.penrose import start

import pytest
from src.get_date import get_date

def test_get_date():
    assert start() == None