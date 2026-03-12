import pytest

from src.checker import check_sign

@pytest.mark.smoke
@pytest.mark.parametrize("a, expected", (
    pytest.param(1, "positive", id="Positive number"),
    pytest.param(-1, "zero or negative", id="Negative number"),
    pytest.param(0, "zero or negative", id="Zero number"),
))
def test_check_sign(a, expected):
    assert check_sign(a) == expected