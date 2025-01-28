import logging
from logging import Logger
from logging.handlers import RotatingFileHandler
from typing import Dict


def setup_logger(name: str, log_file: str, level: int = logging.INFO) -> Logger:
    """
    Настраивает и возвращает логер с указанными параметрами.

    :param name: Имя логера.
    :param log_file: Путь до файла для записи логов.
    :param level: Уровень логирования (по умолчанию INFO).
    :return: Настроенный логер.
    """
    # Создаем логер
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Настраиваем формат сообщений
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Настраиваем обработчик для записи в файл (перезаписываем файл при каждом запуске)
    file_handler = RotatingFileHandler(log_file, mode='w', maxBytes=5 * 1024 * 1024, backupCount=2, encoding='utf-8')
    file_handler.setFormatter(formatter)

    # Добавляем обработчик к логеру
    logger.addHandler(file_handler)

    return logger


# Словарь с настройками логеров для модулей
loggers: Dict[str, Logger] = {
    "utils": setup_logger("utils", "utils.log"),
    "masks": setup_logger("masks", "masks.log"),
}
