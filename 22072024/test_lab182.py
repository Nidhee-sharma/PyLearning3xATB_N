
import pytest
@pytest.mark.smoke
def test_sub0():
    assert 9-9 ==0
@pytest.mark.smoke
def test_sub1():
    assert 2-2 ==0

@pytest.mark.regression
def test_sub3():
    assert 3-3 ==0
@pytest.mark.sanity
def test_sub4():
    assert 4-4 ==0

@pytest.mark.skip
def test_sub4():
    assert 4 - 4 == 0


    #to mark a specific test cases to add anotation like pytest.mark.regression and smoke pytest -m "smoke' root content
    #to match the conrect use -k