import unittest
from unittest.mock import patch
from external_api.external_api import convert_to_rub, get_exchange_rate


class TestExternalAPI(unittest.TestCase):

    @patch("external_api.external_api.requests.get")
    def test_get_exchange_rate(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"rates": {"RUB": 75.0}}
        rate = get_exchange_rate("USD", "RUB")
        self.assertEqual(rate, 75.0)

    @patch("external_api.external_api.requests.get")
    def test_get_exchange_rate_api_error(self, mock_get):
        mock_get.return_value.status_code = 500
        mock_get.return_value.text = "Internal Server Error"
        with self.assertRaises(RuntimeError):
            get_exchange_rate("USD", "RUB")

    @patch("external_api.external_api.get_exchange_rate", return_value=75.0)
    def test_convert_to_rub_usd(self, mock_get_exchange_rate):
        transaction = {"amount": 100, "currency": "USD"}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 7500.0)

    def test_convert_to_rub_rub(self):
        transaction = {"amount": 100, "currency": "RUB"}
        result = convert_to_rub(transaction)
        self.assertEqual(result, 100.0)
