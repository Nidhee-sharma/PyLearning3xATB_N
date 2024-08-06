#fxture - concept in python
#you can use the fixture
#context to the test .
#simlar - pre condition , post condition
import pytest


#Pre Condition - tokeen should be delete , booking ID - Fixture
#test_update_negative 1
#test_Update_positive 2

#setUp and TearDown - Pre and zpost condition

@pytest.fixture()
def is_married():
    return True


def test_i_need_confirm(is_married):
    assert is_married == True

