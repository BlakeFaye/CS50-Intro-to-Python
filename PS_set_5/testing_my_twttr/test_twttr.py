import pytest 
from twttr import shorten

def test_shorten():
    assert shorten("pain") == "pn" 