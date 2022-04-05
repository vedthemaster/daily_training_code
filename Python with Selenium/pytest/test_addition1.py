import pytest

import pytest
@pytest.mark.skip
def test_add_1():
    assert 100+200 == 400,"failed"

@pytest.mark.skip
def test_add_2():
    assert 100+200 == 300,"failed"

@pytest.mark.xfail
def test_add_3():
    assert 15+13 == 28,"failed"
    
def test_add_4():
    assert 15_10 == 40,"failed"

def test_add_5():
    assert 12+2 == 0,"failed"

def test_add_6():
    assert 100+20 == 4545,"failed"