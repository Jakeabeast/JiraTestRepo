import pytest
import sys

#make all files in application folder viewable for test subdirectory
sys.path.append('./')

#import necessary functions here
from processFluid import process, addition

#-----------------------------------------------------------

#add multiple test parameters for unit test
@pytest.mark.parametrize("args, expected", [
    (["Water", "Blood", "Plasma"], True),
    (["Water", "Plasma"], False),
])

def test_process(args, expected):
    print(*args)
    assert process(*args) == expected

#can overrun @pytest.mark.parametrize to create new test variables appropriate for testing new functions
#example shown below

@pytest.mark.parametrize("num1, num2, expected", [
    (1, 0, 1), #1 + 0 = 1 ***note: 1 - 0 also = 1, good to have multiple tests!
    (3, 4, 7), #3 + 4 = 7 ***note: 3 - 4 != 7, this picks up an issue with function
])

def test_addition(num1, num2, expected):
    print(num1, num2)
    assert addition(num1, num2) == expected
