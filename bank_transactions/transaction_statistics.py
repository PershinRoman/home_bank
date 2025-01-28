from typing import List, Dict

def load_transactions_from_json(file_path: str) -> List[Dict]:
    import json
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def load_transactions_from_csv(file_path: str) -> List[Dict]:
    import csv
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def load_transactions_from_xlsx(file_path: str) -> List[Dict]:
    import pandas as pd
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')
