import pytest
import requests

from src.api import get_data, get_status_code_from_response


def test_api_connection_error(mocker):
    mocker.patch(
        "src.api.requests.get",
        side_effect=requests.exceptions.ConnectionError("Api connection error!")
    )

    # Проверяем, что наша функция корректно "пробрасывает"
    # эту ошибку наверх.
    with pytest.raises(requests.exceptions.ConnectionError):
        get_data()

def test_api_response_status_code(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200

    mocker.patch("src.api.requests.get", return_value=mock_response)

    status_code = get_status_code_from_response(mock_response)

    assert status_code == 200
