from pathlib import Path

from datetime import datetime
from utils import five_str_load, function_five_load, load_str, date_last, load_json
JSON_FILE = Path(__file__).resolve().parent / 'operations.json'
file_json = load_json(JSON_FILE)
sorted_data = date_last(file_json)
five_list = load_str(sorted_data)

numb_bank, numb_kart = function_five_load(five_list)
result_strings = []

for string in numb_kart:
    for i in range(0, len(string), 4):
        formatted_string = ' '.join([string[i:i + 4] for i in range(0, len(string), 4)])
        result_strings.append(formatted_string)

for list_bank, s, list_numb in zip(numb_bank, five_str_load, result_strings):
    data_operation = s['date']
    description = s['description']
    name = s['operationAmount']['currency']['name']
    summ_operation = s['operationAmount']['amount']

    date = datetime.strptime(s["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
    to = s['to'][:-14].replace('Счет ', '')
    print(f'{date[:10].replace("-", ".")} {description}\n'
          f'{list_bank} {list_numb} -> Счет **{to[2:]}\n'
          f'{summ_operation} {name}\n')
