from logs.logging_config import loggers
from typing import List, Dict, Any
import json

# Получаем логер для модуля utils
logger = loggers["utils"]


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, возвращается пустой список.

    :param file_path: Путь до JSON-файла.
    :return: Список словарей с данными о транзакциях.
    """
    try:
        logger.info(f"Попытка чтения файла: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if not isinstance(data, list):
                logger.warning(f"Файл {file_path} не содержит список.")
                return []
            logger.info(f"Файл {file_path} успешно прочитан.")
            return data
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}: {e}")
        return []
