import pytest
import logging
import sys
from functools import wraps

# Настройка логирования на уровне модуля
logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logging.info(f"Starting {func.__name__} with args: {args}, kwargs: {kwargs}")
                result = func(*args, **kwargs)
                logging.info(f"{func.__name__} ok: {result}")
                return result
            except Exception as e:
                logging.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise  # Поднимаем ошибку дальше
        return wrapper
    return decorator

@log()
def successful_function(x, y):
    return x + y

@log()
def error_function(x, y):
    return x / y  # Это может привести к ошибке деления на ноль

def test_successful_function(caplog):
    with caplog.at_level(logging.INFO):
        result = successful_function(3, 4)

    assert result == 7

    # Проверка ожидаемых строк в выводе
    assert "Starting successful_function with args: (3, 4), kwargs: {}" in caplog.text
    assert "successful_function ok: 7" in caplog.text

def test_error_function(caplog):
    with caplog.at_level(logging.INFO):
        with pytest.raises(ZeroDivisionError):
            error_function(1, 0)

    # Проверка ожидаемых строк в выводе
    assert "Starting error_function with args: (1, 0), kwargs: {}" in caplog.text
    assert "error_function error: ZeroDivisionError. Inputs: (1, 0), {}" in caplog.text
