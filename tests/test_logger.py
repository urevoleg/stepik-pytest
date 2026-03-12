import pytest

from src.logger import log_message


def test_logger_was_called(mocker):
    mocker_send = mocker.patch("src.logger.external_logger.send")
    mocker_send.send = "Hello!"

    log_message("Hello!")

    mocker_send.assert_called_once_with("Hello!")