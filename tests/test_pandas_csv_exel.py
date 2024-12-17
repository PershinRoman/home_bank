import pandas as pd
from unittest.mock import patch, mock_open
from pandas_exel_csv.pandas_csv_exel import read_csv_file, read_xlsx_file


def test_read_csv_file_valid():
    # Мокаем содержимое CSV-файла
    mock_csv_content = "id,amount,currency\n1,100,USD\n2,200,EUR"
    with patch("builtins.open", mock_open(read_data=mock_csv_content)):
        with patch("pandas.read_csv") as mock_read_csv:
            mock_read_csv.return_value = pd.DataFrame.from_dict([
                {"id": 1, "amount": 100, "currency": "USD"},
                {"id": 2, "amount": 200, "currency": "EUR"}
            ])
            result = read_csv_file("dummy_path.csv")
            assert result == [
                {"id": 1, "amount": 100, "currency": "USD"},
                {"id": 2, "amount": 200, "currency": "EUR"}
            ]


def test_read_csv_file_not_found():
    with patch("pandas.read_csv", side_effect=FileNotFoundError):
        result = read_csv_file("nonexistent.csv")
        assert result == []


def test_read_xlsx_file_valid():
    # Мокаем содержимое XLSX-файла
    mock_xlsx_data = pd.DataFrame.from_dict([
        {"id": 1, "amount": 100, "currency": "USD"},
        {"id": 2, "amount": 200, "currency": "EUR"}
    ])
    with patch("pandas.read_excel") as mock_read_excel:
        mock_read_excel.return_value = mock_xlsx_data
        result = read_xlsx_file("dummy_path.xlsx")
        assert result == [
            {"id": 1, "amount": 100, "currency": "USD"},
            {"id": 2, "amount": 200, "currency": "EUR"}
        ]


def test_read_xlsx_file_not_found():
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        result = read_xlsx_file("nonexistent.xlsx")
        assert result == []
