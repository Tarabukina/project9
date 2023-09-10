from pathlib import Path
import pytest
from src.utils import load_json, date_last, stars_numb, function_five_load, load_str

TESTING_DATA = Path(__file__).resolve().parent / "operations.json"

@pytest.fixture()
def test_load_json():

    expected_data = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-09-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
]

    assert load_json(TESTING_DATA) == expected_data


def test_date_last():
    test_data = [
        {
            "id": 1,
            "date": "2023-09-01T10:00:00",
        },
        {
            "id": 2,
            "date": "2023-09-02T10:00:00",
        },
        {
            "id": 3,
            "date": "2023-09-03T10:00:00",
        }
    ]
    test_data_1 = [
        {
            "id": 1,
            "date": "2023-09-01T10:00:00",
        },
        {
            "id": 2,
            "date": "2022-09-02T10:00:00",
        },
        {
            "id": 3,
            "date": "2024-09-03T10:00:00",
        }
    ]
    expected_result = [
        {
            "id": 3,
            "date": "2023-09-03T10:00:00",
        },
        {
            "id": 2,
            "date": "2023-09-02T10:00:00",
        },
        {
            "id": 1,
            "date": "2023-09-01T10:00:00",
        }
    ]
    sorted_data = date_last(test_data)
    assert sorted_data == expected_result
    assert date_last(test_data_1) == [{'date': '2024-09-03T10:00:00', 'id': 3},
 {'date': '2023-09-01T10:00:00', 'id': 1},
 {'date': '2022-09-02T10:00:00', 'id': 2}]

def test_stars_numb():
    test_numb = ['12312312313323','32132143321321']
    assert stars_numb(test_numb) == ['','284287******9012','781084******5568','386114**********9794','','123123****3323','321321****1321']
def test_function_five_load():
    test_list = [{'from': 'Maestro 13245678789456'},
                 {'from': 'Maestro Viza 13245678789456'}]
    name_bank = ['', 'Visa Classic', 'Maestro', 'Счет', '', 'Maestro', 'Maestro Viza']
    numder_bank = ['','284287******9012','781084******5568','386114**********9794','', '123123****3323', '321321****1321','13245678789456','13245678789456']
    assert function_five_load(test_list) ==(name_bank, numder_bank)

def test_load_str():
    test_load_str_1 = [{'state':'EXECUTED',
                      'id': '1'
                      },
                     {'state': 'FALED',
                      'id': '2'
                      },

                     {'state': 'EXECUTED',
                      'id': '3'
                      },

                     {'state': 'EXECUTED',
                      'id': '4'
                      },

                     {'state': 'EXECUTED',
                      'id': '5'
                      },
                     {'state': 'EXECUTED',
                      'id': '6'
                      }

                     ]
    expected_table = [{'date': '2019-12-08T22:46:21.935582',
  'description': 'Открытие вклада',
  'id': 863064926,
  'operationAmount': {'amount': '41096.24',
                      'currency': {'code': 'USD', 'name': 'USD'}},
  'state': 'EXECUTED',
  'to': 'Счет 90424923579946435907'},
 {'date': '2019-12-07T06:17:14.634890',
  'description': 'Перевод организации',
  'from': 'Visa Classic 2842878893689012',
  'id': 114832369,
  'operationAmount': {'amount': '48150.39',
                      'currency': {'code': 'USD', 'name': 'USD'}},
  'state': 'EXECUTED',
  'to': 'Счет 35158586384610753655'},
 {'date': '2019-11-19T09:22:25.899614',
  'description': 'Перевод организации',
  'from': 'Maestro 7810846596785568',
  'id': 154927927,
  'operationAmount': {'amount': '30153.72',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'state': 'EXECUTED',
  'to': 'Счет 43241152692663622869'},
 {'date': '2019-11-13T17:38:04.800051',
  'description': 'Перевод со счета на счет',
  'from': 'Счет 38611439522855669794',
  'id': 482520625,
  'operationAmount': {'amount': '62814.53',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'state': 'EXECUTED',
  'to': 'Счет 46765464282437878125'},
 {'date': '2019-11-05T12:04:13.781725',
  'description': 'Открытие вклада',
  'id': 801684332,
  'operationAmount': {'amount': '21344.35',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'state': 'EXECUTED',
  'to': 'Счет 77613226829885488381'},
 {'id': '1', 'state': 'EXECUTED'},
 {'id': '3', 'state': 'EXECUTED'},
 {'id': '4', 'state': 'EXECUTED'},
 {'id': '5', 'state': 'EXECUTED'},
 {'id': '6', 'state': 'EXECUTED'}]
    assert load_str(test_load_str_1) == expected_table