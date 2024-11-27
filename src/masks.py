def get_mask_card_number(card_number: str) -> str:
    """Преобразуем номер карты в строку(на случай, если передан int)"""
    card_number = str(card_number)

    """Проверяем длину номера карты"""
    if len(card_number) != 16:
        raise ValueError("Номер карты не соответсвует количеству 16 цифр.")

    """Формируем замаскированный код используя срезы"""

    masked_number = (card_number[:4] + " " + card_number[4:6] + "** ****" + card_number[-4:])

    """(flake8 выдавал ошибку, разбил на разные строки)"""
    return masked_number


def get_mask_account(account_number: str) -> str:
    """Преобразуем номер счета в строку"""
    account_number = str(account_number)

    """Проверяем длину строки номера счета"""
    if len(account_number) < 4:
        raise ValueError("Номер счета должен состоять из 4 символов.")

    """Маскируем номер"""
    masked_account = "**" + account_number[-4:]
    return masked_account
