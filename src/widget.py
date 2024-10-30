def get_mask_account(account_number: str) -> str:
    """
    Маскируем номер счета.
    Показывает только последние 4 цифры,
    заменяет остальные цифры - символом
    """
    # Преобразуем номер счета в строку
    account_number = str(account_number)

    # Проверяем длину строки номера счета
    if len(account_number) < 4:
        raise ValueError("Номер счета должен состоять из 4 символов.")

    # Маскируем номер
    masked_account = "**" + account_number[-4:]
    return masked_account


def get_mask_card_number(card_number: str) -> str:
    """
    Маскируем номер карты.
    Показывает первые 4 и последние 4 цифры
    Остальные заменяем символом
    """
    # Преобразуем номер карты в строку(на случай, если передан int)
    card_number = str(card_number)

    # Проверяем длину номера карты
    if len(card_number) != 16:
        raise ValueError("Номер карты не соответсвует количеству 16 цифр.")

    # Формируем замаскированный код используя срезы
    masked_number = card_number[:4] + " " + card_number[4:6] + "** ****" + card_number[-4:]

    # (flake8 выдавал ошибку, разбил на разные строки)
    return masked_number


def mask_account_card(name_card: str) -> str:
    parts = name_card.split()
    type_card = " ".join(parts[:-1])  # Составлет тип карты
    number_card = parts[-1]  # Последняя часть - номер

    if name_card.lower() in ["счет"]:  # Тип, есть - счет
        return f"{type_card} {mask_account_card(number_card)}"
    else:  # Для карта
        return f"{type_card} {get_mask_account(number_card)}"


print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361
print(mask_account_card("Счет 73654108430135874305"))  # Счет 4305
print(mask_account_card("Maestro 1596837868705199"))  # Maestro 1596 83 **** 5199
print(mask_account_card("Счет 64686473678894779589"))  # Счет **9589
