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
    (3, 4, 7),
    (1, 0, 1),
])
