import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv('.env')  # Загружаем переменные окружения из .env

API_URL = "https://api.apilayer.com/exchangerates_data/latest"


def get_exchange_rate(base_currency: str, target_currency: str) -> float:
    """
    Получает текущий курс обмена валют через API.
    """
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY не задан в .env")

    headers = {"apikey": api_key}
    params = {"base": base_currency, "symbols": target_currency}
    response = requests.get(API_URL, headers=headers, params=params)

    if response.status_code != 200:
        raise RuntimeError(f"Ошибка API: {response.status_code}, {response.text}")

    rates = response.json().get("rates", {})
    return rates.get(target_currency, 1.0)


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.
    Если валюта не указана, возвращает сумму как есть.
    """
    amount = transaction.get("amount", 0.0)
    currency = transaction.get("currency", "RUB")

    if currency == "RUB":
        return float(amount)  # Уже в рублях

    exchange_rate = get_exchange_rate(currency, "RUB")
    return float(amount) * exchange_rate
