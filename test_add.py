import pytest
import app
def test_add():
    assert app.add(2,3)==5

def test_sub():
    assert app.sub(2,3)==-1
def test_mult():
    assert app.mult(10,2) == 20
