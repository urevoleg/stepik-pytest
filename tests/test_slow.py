import time

import pytest

@pytest.mark.slow_slow
def test_slow_1():
    time.sleep(1)
    assert True


@pytest.mark.slow_slow
def test_slow_2():
    time.sleep(1)
    assert True


@pytest.mark.slow_slow
def test_slow_3():
    time.sleep(1)
    assert True


@pytest.mark.slow_slow
def test_slow_4():
    time.sleep(1)
    assert True