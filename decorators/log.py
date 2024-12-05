import logging
import sys
from functools import wraps

def log(filename=None):
    # Настройка логирования
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
    else:
        logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

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

# Пример использования декоратора
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

@log()
def my_error_function(x, y):
    return x / y  # Это может привести к ошибке деления на ноль

# Вызов функций
my_function(1, 2)          # Логи будут записаны в mylog.txt
try:
    my_error_function(1, 0)    # Логи будут выведены в консоль
except ZeroDivisionError:
    pass  # Обработка ошибки, если нужно