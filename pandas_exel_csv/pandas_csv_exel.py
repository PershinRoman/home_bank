import pandas as pd
from typing import List, Dict, Any


def read_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает CSV-файл и возвращает список словарей с данными о финансовых транзакциях.

    :param file_path: Путь до CSV-файла.
    :return: Список словарей с данными о транзакциях.
    """
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except pd.errors.EmptyDataError:
        print(f"Файл {file_path} пустой.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла {file_path}: {e}")
        return []


def read_xlsx_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает XLSX-файл и возвращает список словарей с данными о финансовых транзакциях.

    :param file_path: Путь до XLSX-файла.
    :return: Список словарей с данными о транзакциях.
    """
    try:
        df = pd.read_excel(file_path, engine="openpyxl")
        return df.to_dict(orient="records")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except ValueError:
        print(f"Файл {file_path} пустой или имеет неправильный формат.")
        return []
    except Exception as e:
        print(f"Ошибка при чтении XLSX-файла {file_path}: {e}")
        return []
