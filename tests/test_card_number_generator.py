import pytest

from generators.card_number_generator import card_number_generator


def test_card_number_generator():
    '''
    Проверяют, как эта функция работает с различными входными данными, включая пустой список.
    '''
    # Проверяем генерацию карт с диапазоном от 1 до 5
    expected_card_numbers = [
        '0000000000000001',
        '0000000000000002',
        '0000000000000003',
        '0000000000000004',
        '0000000000000005'
    ]

    generated_card_numbers = list(card_number_generator(1, 5))
    assert generated_card_numbers == expected_card_numbers

    # Проверяем генерацию карт с диапазоном от 10 до 15
    expected_card_numbers_10_to_15 = [
        '0000000000000010',
        '0000000000000011',
        '0000000000000012',
        '0000000000000013',
        '0000000000000014',
        '0000000000000015'
    ]

    generated_card_numbers_10_to_15 = list(card_number_generator(10, 15))
    assert generated_card_numbers_10_to_15 == expected_card_numbers_10_to_15

    # Проверяем крайние значения: минимальный диапазон
    assert list(card_number_generator(1, 1)) == ['0000000000000001']
    assert list(card_number_generator(100, 100)) == ['0000000000000100']

    # Проверяем крайние значения: пустой диапазон
    empty_generated_numbers = list(card_number_generator(1, 0))
    assert empty_generated_numbers == []  # Проверяем, что с пустым диапазоном ничего не генерируется

    # Проверяем генерацию карт с диапазоном от 999995 до 1000000
    expected_large_range = [
        '0000000000999995',
        '0000000000999996',
        '0000000000999997',
        '0000000000999998',
        '0000000000999999',
        '0000000001000000'
    ]

    generated_large_range = list(card_number_generator(999995, 1000000))
    assert generated_large_range == expected_large_range


@pytest.mark.parametrize("start, end, expected", [
    (1, 5, [
        '0000000000000001',
        '0000000000000002',
        '0000000000000003',
        '0000000000000004',
        '0000000000000005'
    ]),
    (10, 12, [
        '0000000000000010',
        '0000000000000011',
        '0000000000000012'
    ]),
    (0, 2, [
        '0000000000000000',
        '0000000000000001',
        '0000000000000002'
    ]),
])
def test_card_number_generator(start, end, expected):
    generated_numbers = list(card_number_generator(start, end))
    assert generated_numbers == expected
