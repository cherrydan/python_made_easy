import pytest

import cubefunc


@pytest.mark.parametrize("arg, expected_res", [(2.23, 2.0), (5, 24.00), (10, 192)])
def test_capacity(arg, expected_res):
    assert cubefunc.cube_capacity(arg) == expected_res


@pytest.mark.parametrize("arg, expected_res", [(2.23, 9.9458), (5, 50.00), (10, 200)])
def test_square(arg, expected_res):
    assert cubefunc.cube_square(arg) == expected_res


@pytest.mark.parametrize("arg1, arg2, arg3, expected_res", [(3, 4, 5, 6), (2, 3, 4, 5)])
def test_newcube(arg1, arg2, arg3, expected_res):
    assert cubefunc.new_cube(arg1, arg2, arg3) == expected_res
