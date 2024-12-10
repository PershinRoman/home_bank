import unittest
from unittest.mock import patch, mock_open
from utils.utils import load_transactions


class TestUtils(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
    def test_load_transactions_valid(self, mock_file):
        result = load_transactions("dummy_path.json")
        self.assertEqual(result, [{"amount": 100, "currency": "USD"}])

    @patch("builtins.open", new_callable=mock_open, read_data='')
    def test_load_transactions_empty_file(self, mock_file):
        result = load_transactions("dummy_path.json")
        self.assertEqual(result, [])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_transactions_file_not_found(self, mock_file):
        result = load_transactions("dummy_path.json")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
    def test_load_transactions_not_a_list(self, mock_file):
        result = load_transactions("dummy_path.json")
        self.assertEqual(result, [])
