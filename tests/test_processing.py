import pytest

from src.processing import filter_by_state, sort_by_date

if __name__ == '__main__':
    pytest.main()

transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
]


def test_filter_by_state():
    '''проверка функции на правильное возвращение транзакций со статусом executed
    на правильное возвращение транзакций со статусом canceled
    возвращает пустой список, если передан неизвестный статус'''
    executed = filter_by_state(transactions)
    assert len(executed) == 2
    assert executed == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]
    canceled = filter_by_state(transactions, 'CANCALED')
    assert len(canceled) == 0
    assert canceled == []

    emty = filter_by_state(transactions, 'UNKNOWN')
    assert len(emty) == 0


def test_sort_by_date():
    '''Проверка правильности сортировки стандартов по дате в порядке убывания и возрастания'''
    sorted_desc = sort_by_date(transactions)
    assert sorted_desc == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    ]

    sorted_asc = sort_by_date(transactions, descending=False)
    assert sorted_asc == [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},

    ]
