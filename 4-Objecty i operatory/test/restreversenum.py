import pytest

from reverse_num import reverse_num_math


@pytest.mark.parametrize("arg, expected_res", [(123456, 654321), (13243546, 64534231)])
def test(arg, expected_res):
    assert reverse_num_math(arg) == expected_res
