import json
from pathlib import Path
JSON_FILE = Path(__file__).resolve().parent / 'operations.json'

def load_json(file_path):
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
        return data


file_json = load_json(JSON_FILE)


def date_last(UP):
    '''функция сортирует все значения по дате от наименьшего к наибольшему'''
    sorted_data_1 = sorted(UP, key=lambda x: x.get('date'), reverse=True)
    return sorted_data_1




# создаем пустой список для записи первых 5 значений
five_str_load = []


def load_str(resorted):
    '''функция записи последних элементов со статусом "EXECUTED",
    если статус ==EXECUTED, то переменная счетчик увеличивается на 1
    и происходит запись в словарь, как только переменная счетчик будет равна 5, цикл автоматом вырубается'''
    count = 0

    for state_status in resorted:
        state = state_status.get('state', '')

        if state == 'EXECUTED':
            five_str_load.append(state_status)
            count += 1

        if count == 5:
            break
    return five_str_load




# создаем 2 списка для записи в них наименования банка и наименоваие счета
numb_bank = [] # имя банка
numb_kart = [] # имя счета


def function_five_load(an):
    '''функция извлекает все статусы из списка и разделяет
    далее через сплит разделяет по пробелу все значения и записывает их в новые списки'''

    for r in an:
        from_1 = r.get('from', '')
        w = from_1.split(' ')

        numb_bank.append(' '.join(w[:-1]))
        numb_kart.append(''.join(w[-1]))
    #print(numb_bank)
   # print(numb_kart)
    return numb_bank, numb_kart




# создаем пустой список, чтобы добавить звездочки, вместе символов

replay_numb_kart = []


def stars_numb(q):
    '''функция для преобразования некоторых чисел в звездочки
    и записи их в новый список'''
    for o in q:
        stars = len(o) - 10

        replay_numb_kart.append(o[:6] + "*" * stars + o[-4:])
    return replay_numb_kart







