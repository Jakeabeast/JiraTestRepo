import pytest

from processFluid import process

#add multiple test parameters for unit test
@pytest.mark.parametrize("args, expected", [
    (*["Water", "Blood", "Plasma"], True),
    (*["Water", "Plasma"], False),
])

def test_process(args, expected):
    print(args)
    assert process(args) == expected
