def transaction_descriptions(transactions):
    '''
    Генератор перебирает список транзакций
    и возвращает соответствующее описание
    в зависимости от типа транзакций.
    '''
    for transaction in transactions:
        if transaction['type'] == 'transfer':
            yield 'Перевод со счета на счет'
        elif transaction['type'] == 'card_transfer':
            yield 'Перевод с карты на карту'
        elif transaction['type'] == 'organization_transfer':
            yield 'Перевод организации'
        else:
            yield 'Неизвестная операция'


transactions = [
    {'type': 'transfer'},
    {'type': 'transfer'},
    {'type': 'card_transfer'},
    {'type': 'organization_transfer'},
    {'type': 'unknown_transfer'},  # Неизвестная операция
]

# Использование генератора
descriptions = transaction_descriptions(transactions)
for description in descriptions:
    print(description)
