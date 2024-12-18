import os
import requests
from typing import Dict, Any


def convert_to_rubles(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли, если она указана в USD или EUR.
    Если транзакция уже в рублях, возвращает сумму без изменений.

    :param transaction: Словарь с данными о транзакции.
    :return: Сумма транзакции в рублях.
    """
    # Извлекаем сумму и валюту из вложенного словаря
    operation_amount = transaction.get("operationAmount", {})
    amount = float(operation_amount.get("amount", 0))
    currency_info = operation_amount.get("currency", {})
    currency = currency_info.get("code", "RUB")

    if currency == "RUB":
        return amount

    # Получаем API-ключ из переменных окружения
    api_key = os.getenv('EXCHANGE_API_KEY')
    if not api_key:
        raise ValueError("Не найден API-ключ для конвертации валюты. Проверьте файл .env.")

    # Обращаемся к API для получения курса валют
    url = f"https://api.apilayer.com/exchangerates_data/convert"
    params = {
        "from": currency,
        "to": "RUB",
        "amount": amount
    }
    headers = {"apikey": api_key}

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    data = response.json()
    return float(data.get("result", 0))
