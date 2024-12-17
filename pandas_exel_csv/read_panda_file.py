from pandas_exel_csv.pandas_csv_exel import read_csv_file, read_xlsx_file

csv_transactions = read_csv_file("transactions.csv")
print(csv_transactions)

xlsx_transactions = read_xlsx_file("transactions_excel.xlsx")
print(xlsx_transactions)