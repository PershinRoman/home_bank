import pytest
from generators.transaction_discriptions import transaction_descriptions


def test_transaction_descriptions():
    '''
    Проверяет, что функция возвращает правильные описания для известного списка транзакций.
    Проверяет, что функция возвращает пустой список, если входной список пуст.
    Проверяет, что функция возвращает описание для неизвестных типов транзакций.
    '''
    # Тестируем с несколькими транзакциями
    transactions = [
        {'type': 'transfer'},
        {'type': 'transfer'},
        {'type': 'card_transfer'},
        {'type': 'organization_transfer'},
        {'type': 'unknown_transfer'}
    ]

    expected_descriptions = [
        'Перевод со счета на счет',
        'Перевод со счета на счет',
        'Перевод с карты на карту',
        'Перевод организации',
        'Неизвестная операция'
    ]

    assert list(transaction_descriptions(transactions)) == expected_descriptions

    # Тестируем с пустым списком
    empty_transactions = []
    expected_empty_descriptions = []

    assert list(transaction_descriptions(empty_transactions)) == expected_empty_descriptions

    # Тестируем с транзакциями без описаний
    transactions_without_descriptions = [
        {'type': 'unknown_transfer'},
        {'type': 'unknown_transfer'}
    ]

    expected_no_descriptions = ['Неизвестная операция', 'Неизвестная операция']

    assert list(transaction_descriptions(transactions_without_descriptions)) == expected_no_descriptions


@pytest.mark.parametrize("transactions, expected_descriptions", [
    (
        [
            {'type': 'transfer'},
            {'type': 'transfer'},
            {'type': 'card_transfer'},
            {'type': 'organization_transfer'},
            {'type': 'unknown_transfer'}
        ],
        [
            'Перевод со счета на счет',
            'Перевод со счета на счет',
            'Перевод с карты на карту',
            'Перевод организации',
            'Неизвестная операция'
        ]
    ),
    (
        [],  # Пустой список
        []
    ),
    (
        [
            {'type': 'unknown_transfer'},
            {'type': 'unknown_transfer'}
        ],
        [
            'Неизвестная операция',
            'Неизвестная операция'
        ]
    )
])
def test_transaction_descriptions(transactions, expected_descriptions):
    assert list(transaction_descriptions(transactions)) == expected_descriptions
