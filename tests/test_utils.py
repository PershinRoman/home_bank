from unittest.mock import mock_open, patch

from utils.utils import read_json_file


def test_read_json_file_valid():
    mock_json_data = '[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]'
    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        result = read_json_file("dummy_path.json")
    assert result == [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]


def test_read_json_file_empty():
    mock_json_data = ''
    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        result = read_json_file("dummy_path.json")
    assert result == []


def test_read_json_file_not_list():
    mock_json_data = '{"id": 1, "amount": 100}'
    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        result = read_json_file("dummy_path.json")
    assert result == []

    def test_read_json_file_not_found():
        with patch("builtins.open", side_effect=FileNotFoundError):
            result = read_json_file("nonexistent_file.json")
        assert result == []
