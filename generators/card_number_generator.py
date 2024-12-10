def card_number_generator(start, end):
    '''
    генератор принимает начальное и конечное значения,
    затем создает номера карт,
    используя форматирование строк для добвления пробелов
    и заполнения нулями
    '''
    for number in range(start, end + 1):
        card_number = f'{number:016d}'  # Форматируем номер, заполняя нулями до 16 цифр
        yield card_number  # Возвращаем только отформатированный номер


for card_number in card_number_generator(1, 5):
    print(card_number)
