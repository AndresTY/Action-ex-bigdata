import pytest
import app
def test_add():
    assert app.add(2,3)==5

def test_sub():
    assert app.sub(2,3)==-1
