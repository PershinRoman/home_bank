from generators.filter_by_currency import filter_by_currency


def test_filter_by_currency():
    '''
    проверяет, правильно ли функция фильтрует транзакции по заданному коду валюты.
    '''
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 123456789,
            "state": "EXECUTED",
            "date": "2020-01-01T12:00:00.000000",
            "operationAmount": {
                "amount": "500.00",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 12345678901234567890",
            "to": "Счет 09876543210987654321"
        }
    ]
    # Тестируем фильтрацию по USD
    usd_transactions = list(filter_by_currency(transactions, 'USD'))
    assert len(usd_transactions) == 2
    assert usd_transactions[0]['id'] == 939719570
    assert usd_transactions[1]['id'] == 142264268

    # Тестируем фильтрацию по EUR
    eur_transactions = list(filter_by_currency(transactions, 'EUR'))
    assert len(eur_transactions) == 1
    assert eur_transactions[0]['id'] == 123456789

    # Тестируем фильтрацию по несуществующей валюте
    unknown_transactions = list(filter_by_currency(transactions, 'JPY'))
    assert len(unknown_transactions) == 0
