import pytest

import cubefunc


@pytest.mark.parametrize("arg, expected_res", [(2.23, 2.0), (5, 24.00), (10, 192)])
def test_capacity(arg, expected_res):
    assert cubefunc.cube_capacity(arg) == expected_res


@pytest.mark.parametrize("arg, expected_res", [(2.23, 9.9458), (5, 50.00), (10, 200)])
def test_square(arg, expected_res):
    assert cubefunc.cube_square(arg) == expected_res
