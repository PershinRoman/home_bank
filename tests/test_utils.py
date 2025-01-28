from utils.utils import read_json_file
from unittest.mock import patch, mock_open


def test_read_json_file_valid():
    mock_data = '''
    [
      {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
          "amount": "8221.37",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
      }
    ]
    '''
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json_file("operations.json")
        assert len(result) == 1
        assert result[0]["id"] == 41428829


def test_read_json_file_empty():
    with patch("builtins.open", mock_open(read_data="")):
        result = read_json_file("operations.json")
        assert result == []


def test_read_json_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_json_file("nonexistent.json")
        assert result == []
