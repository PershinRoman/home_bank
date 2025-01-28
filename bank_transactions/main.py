import json
from transaction_filter import filter_transactions_by_description, count_operations_by_category
from transaction_statistics import load_transactions_from_json, load_transactions_from_csv, load_transactions_from_xlsx

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    if choice == '1':
        file_path = input("Введите путь к JSON-файлу: ")
        transactions = load_transactions_from_json(file_path)
    elif choice == '2':
        file_path = input("Введите путь к CSV-файлу: ")
        transactions = load_transactions_from_csv(file_path)
    elif choice == '3':
        file_path = input("Введите путь к XLSX-файлу: ")
        transactions = load_transactions_from_xlsx(file_path)
    else:
        print("Неверный выбор.")
        return

    status = input("Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): ").strip().lower()
    valid_statuses = ['executed', 'canceled', 'pending']

    while status not in valid_statuses:
        print(f"Статус операции \"{status.upper()}\" недоступен.")
        status = input("Введите статус, по которому необходимо выполнить фильтрацию (EXECUTED, CANCELED, PENDING): ").strip().lower()

    filtered_transactions = [t for t in transactions if t.get('state', '').lower() == status]
    print(f"Операции отфильтрованы по статусу \"{status.upper()}\".")

    sort = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort == 'да':
        order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        reverse = order == 'по убыванию'
        filtered_transactions.sort(key=lambda x: x.get('date'), reverse=reverse)

    currency_filter = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if currency_filter == 'да':
        filtered_transactions = [t for t in filtered_transactions if t.get('currency') == 'руб.']

    description_filter = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if description_filter == 'да':
        search_string = input("Введите строку для поиска: ")
        filtered_transactions = filter_transactions_by_description(filtered_transactions, search_string)

    print("Распечатываю итоговый список транзакций...")
    if filtered_transactions:
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            print(f"{transaction['date']} {transaction['description']}")
            print(f"Счет **{transaction['account']}")
            print(f"Сумма: {transaction['amount']} {transaction['currency']}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

if __name__ == "__main__":
    main()
