import os

import pytest

FILENAME = "state.txt"


@pytest.mark.depends
def test_create_file():
    with open(FILENAME, "w") as f:
        f.write("hello")
    assert os.path.exists(FILENAME)


@pytest.mark.depends
def test_read_file():
    # Этот тест упадет, если запустится РАНЬШЕ test_create_file
    with open(FILENAME, "r") as f:
        content = f.read()
    assert content == "hello"