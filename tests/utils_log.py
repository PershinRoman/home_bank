from logs.utils import read_json_file
from unittest.mock import mock_open, patch
import logging


@patch("builtins.open", mock_open(read_data='[{"id": 1, "amount": 100}]'))
def test_read_json_file_with_logging(caplog):
    with caplog.at_level(logging.INFO):
        result = read_json_file("dummy_path.json")
        assert result == [{"id": 1, "amount": 100}]
        assert "Попытка чтения файла: dummy_path.json" in caplog.text
        assert "Файл dummy_path.json успешно прочитан." in caplog.text
