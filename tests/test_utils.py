import pytest

from src.utils import is_even


@pytest.mark.parametrize("number, expected_result", (
    (2, True),
    (1, False),
    (0, True),
    (-4, True),
    (-5, False)
))
def test_is_event_with_various_numbers(number, expected_result):
    assert is_even(number) ==  expected_result