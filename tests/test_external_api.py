import os
from unittest.mock import patch
from external_api.external_api import convert_to_rubles


@patch("external_api.external_api.requests.get")
def test_convert_to_rubles_usd(mock_get):
    # Мокаем ответ от API
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 600.0}

    transaction = {
        "operationAmount": {
            "amount": "10",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        }
    }

    with patch.dict(os.environ, {"EXCHANGE_API_KEY": "test_key"}):
        result = convert_to_rubles(transaction)
        assert result == 600.0


@patch("external_api.external_api.requests.get")
def test_convert_to_rubles_rub(mock_get):
    transaction = {
        "operationAmount": {
            "amount": "1000",
            "currency": {
                "name": "RUB",
                "code": "RUB"
            }
        }
    }

    result = convert_to_rubles(transaction)
    assert result == 1000.0
    mock_get.assert_not_called()
