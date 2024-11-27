def filter_by_state(transactions, state='EXECUTED') -> dict[str, int]:
    '''Функция принимает два аргумента,
     список transaction и строку state,
      которая равно по условию EXECUTED'''

    return [transaction for transaction in transactions if transaction.get("state") == state]

# Создание нового списка с помощью генератора списка.
# Он перебирает каждый элемент и добавляет новый список,
# при выполненных условиях

# Метод get для безопасного получения значения по ключу,
# на случай если ключ отсутсвует


''' Выход функции со статусом по умолчанию 'EXECUTED' '''

transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
]

executed_transactions = filter_by_state(transactions)
print('EXECUTED', executed_transactions)
# Выход функции, если вторым аргументом передано 'CANCELED'
canceled_transaction = filter_by_state(transactions, 'CANCELED')
print('CACELED', canceled_transaction)


def sort_by_date(transactions, descending=True) -> dict[str, int]:
    '''Функция принимает два аргумента:
    список словарей и булевый параметр, который указывает,
    нужно ли сортировать в порядке убывания'''
    # сортируем список по дате
    return sorted(transactions, key=lambda x: x['date'], reverse=descending)


transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
]

'''Сортировка по убыванию'''
sorted_transactions_desc = sort_by_date(transactions)
print('sorted (descending):', sorted_transactions_desc)

'''По возрастанию'''
sorted_transactions_asc = sort_by_date(transactions, descending=False)
print('sorted (ascending):', sorted_transactions_asc)
