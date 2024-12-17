from unittest.mock import patch

from external_api.external_api import convert_to_rubles


@patch("external_api.external_api.requests.get")
@patch("os.getenv", return_value="test_api_key")
def test_convert_to_rubles_usd(mock_getenv, mock_requests_get):
    mock_response = {
        "result": 7500.0
    }
    mock_requests_get.return_value.json.return_value = mock_response
    mock_requests_get.return_value.raise_for_status = lambda: None

    transaction = {"amount": 100, "currency": "USD"}
    result = convert_to_rubles(transaction)
    assert result == 7500.0
    mock_requests_get.assert_called_once()


@patch("external_api.external_api.requests.get")
@patch("os.getenv", return_value="test_api_key")
def test_convert_to_rubles_rub(mock_getenv, mock_requests_get):
    transaction = {"amount": 100, "currency": "RUB"}
    result = convert_to_rubles(transaction)
    assert result == 100.0
    mock_requests_get.assert_not_called()


@patch("external_api.external_api.requests.get")
@patch("os.getenv", return_value=None)
def test_convert_to_rubles_no_api_key(mock_getenv, mock_requests_get):
    transaction = {"amount": 100, "currency": "USD"}
    try:
        convert_to_rubles(transaction)
        assert False, "Ожидалось ValueError при отсутствии API-ключа"
    except ValueError as e:
        assert str(e) == "Не найден API-ключ для конвертации валюты. Проверьте файл .env."
