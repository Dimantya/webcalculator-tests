# -*- coding: cp1251 -*-

import requests
import os

url_get = 'http://127.0.0.1:17678/api/state'
url_addition = 'http://127.0.0.1:17678/api/addition'
url_multiplication = 'http://127.0.0.1:17678/api/multiplication'
url_division = 'http://127.0.0.1:17678/api/division'
url_remainder = 'http://127.0.0.1:17678/api/remainder'

right_values = {'x': 42, 'y': 24}
high_value = {'x': 42, 'y': 21474836478}
low_value = {'x': 42, 'y': -2147483649}
fractional_value = {'x': 42, 'y': 24.5}
limit_values = {'x': -2147483648, 'y': 21474836447}
underlimit_values = {'x': -2147483647, 'y': 2147483646}
zero_value = {'x': 42, 'y': 0}


def test_start():
    print('\n\n<<Проверка запуска, остановки и рестарта приложения webcalculator.exe>>')
    print('\n\n<Старт на стандартном адресе и порте 127.0.0.1:17678>')
    os.system("webcalculator.exe start")
    print('\n\n<Попытка повторного старта при уже запущенном приложении>')
    os.system("webcalculator.exe start")
    print('\n\n<Перезапуск работы приложения, проверка сохранения адреса и порта с прошлого запуска: 127.0.0.1:17678>')
    os.system("webcalculator.exe restart")
    print('\n\n<Остановка работы приложения>')
    os.system("webcalculator.exe stop")
    print('\n\n<Старт на стандартном адресе 127.0.0.1 и порте 5413>')
    os.system("webcalculator.exe start localhost 5413")
    print('\n\n<Перезапуск работы приложения, проверка сохранения адреса и порта с прошлого запуска: 127.0.0.1: 5413>')
    os.system("webcalculator.exe restart")
    print('\n\n<Остановка работы приложения>')
    os.system("webcalculator.exe stop")
    print('\n\n<Старт приложения на адресе 127.2.5.10 и порте 5413>')
    os.system("webcalculator.exe start 127.2.5.10 5413")
    print('\n\n<Перезапуск работы приложения, проверка сохранения адреса и порта с прошлого запуска: 127.2.5.10 и порте 5413>')
    os.system("webcalculator.exe restart")
    print('\n\n<Остановка работы приложения>')
    os.system("webcalculator.exe stop")

def test_get():
    print('\n\n<<Проверка get-запроса о статусе сервера>>')
    os.system("webcalculator.exe start")
    get_response = requests.get(url_get)
    print('\n\nСостояние сервера: ', get_response.json())
    assert get_response.json() == {'statusCode': 0, 'state': 'OК'}


def test_addition():
    print('\n\n<<Проверка post-запроса для операции сложения>>')
    post_addition = requests.post(url_addition, json=right_values)
    print('\n\nРезультат сложения с допустимыми значениями х=42 у=24 - ', post_addition.json())
    assert post_addition.json() == {'statusCode': 0, 'result': 66}
    post_addition = requests.post(url_addition, json=high_value)
    print('Результат сложения с числом больше диапазона х=42 у=21474836478 - ', post_addition.json())
    assert post_addition.json() == {'statusCode': 4, 'statusMessage': 'Превышены максимальные значения параметров'}
    post_addition = requests.post(url_addition, json=low_value)
    print('Результат сложения с числом меньше диапазона х=42 у=-2147483649 - ', post_addition.json())
    assert post_addition.json() == {'statusCode': 4, 'statusMessage': 'Превышены максимальные значения параметров'}
    post_addition = requests.post(url_addition, json=fractional_value)
    print('Результат сложения с дробным числом х=42 у=24.5 - ', post_addition.json())
    assert post_addition.json() == {'statusCode': 3, 'statusMessage': 'Значения параметров должны быть целыми'}
    post_addition = requests.post(url_addition, json=limit_values)
    print('Результат сложения пограничных чисел х=-2147483648 у=21474836447 - ', post_addition.json())
    assert post_addition.json() == {'statusCode': 4, 'statusMessage': 'Превышены максимальные значения параметров'}
    post_addition = requests.post(url_addition, json=underlimit_values)
    print('Результат сложения чисел меньше предела х=-2147483647 у=2147483646 - ', post_addition.json())
    assert post_addition.json() == {'statusCode': 0, 'result': -1}

def test_multiplication():
    print('\n\n<<Проверка post-запроса для операции умножения>>')
    post_multiplication = requests.post(url_multiplication, json=right_values)
    print('\n\nРезультат умножения с допустимыми значениями х=42 у=24 - ', post_multiplication.json())
    assert post_multiplication.json() == {'statusCode': 0, 'result': 1008}
    post_multiplication = requests.post(url_multiplication, json=high_value)
    print('Результат умножения с числом больше диапазона х=42 у=21474836478 - ', post_multiplication.json())
    assert post_multiplication.json() == {'statusCode': 4, 'statusMessage': 'Превышены максимальные значения параметров'}
    post_multiplication = requests.post(url_addition, json=low_value)
    print('Результат умножения с числом меньше диапазона х=42 у=-2147483649 - ', post_multiplication.json())
    assert post_multiplication.json() == {'statusCode': 4, 'statusMessage': 'Превышены максимальные значения параметров'}
    post_multiplication = requests.post(url_multiplication, json=fractional_value)
    print('Результат умножения с дробным числом х=42 у=24.5 - ', post_multiplication.json())
    assert post_multiplication.json() == {'statusCode': 3, 'statusMessage': 'Значения параметров должны быть целыми'}
    post_multiplication = requests.post(url_multiplication, json=limit_values)
    print('Результат умножения пограничных чисел х=-2147483648 у=21474836447 - ', post_multiplication.json())
    assert post_multiplication.json() == {'statusCode': 4, 'statusMessage': 'Превышены максимальные значения параметров'}
    post_multiplication = requests.post(url_multiplication, json=underlimit_values)
    print('Результат умножения чисел меньше предела - ', post_multiplication.json())
    assert post_multiplication.json() == {'statusCode': 0, 'result': -4611686011984936962}


def test_division():
    print('\n\n<<Проверка post-запроса для операции деления>>')
    post_division = requests.post(url_division, json=right_values)
    print('\n\nРезультат деления с допустимыми значениями х=42 у=24 - ', post_division.json())
    assert post_division.json() == {'statusCode': 0, 'result': 1}
    post_division = requests.post(url_division, json=high_value)
    print('Результат деления с числом больше диапазона х=42 у=21474836478 - ', post_division.json())
    assert post_division.json() == {'statusCode': 4, 'statusMessage': 'Превышены максимальные значения параметров'}
    post_division = requests.post(url_division, json=low_value)
    print('Результат деления с числом меньше диапазона х=42 у=-2147483649 - ', post_division.json())
    assert post_division.json() == {'statusCode': 4, 'statusMessage': 'Превышены максимальные значения параметров'}
    post_division = requests.post(url_division, json=fractional_value)
    print('Результат деления с дробным числом х=42 у=24.5 - ', post_division.json())
    assert post_division.json() == {'statusCode': 3, 'statusMessage': 'Значения параметров должны быть целыми'}
    post_division = requests.post(url_division, json=limit_values)
    print('Результат деления пограничных чисел х=-2147483648 у=21474836447 - ', post_division.json())
    assert post_division.json() == {'statusCode': 4, 'statusMessage': 'Превышены максимальные значения параметров'}
    post_division = requests.post(url_division, json=underlimit_values)
    print('Результат деления чисел меньше предела х=-2147483647 у=2147483646 - ', post_division.json())
    assert post_division.json() == {'statusCode': 0, 'result': -2}
    post_division = requests.post(url_division, json=zero_value)
    print('Результат деления ноль х=42 у=0 - ', post_division.json())
    assert post_division.json() == {'statusCode': 8, 'statusMessage': 'Ошибка вычисления'}

def test_remainder():
    print('\n\n<<Проверка post-запроса для операции остатка от деления>>')
    post_remainder = requests.post(url_remainder, json=right_values)
    print('\n\nРезультат остатка от деления с допустимыми значениями х=42 у=24 - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 0, 'result': 18}
    post_remainder = requests.post(url_division, json=high_value)
    print('Результат остатка от деления с числом больше диапазона х=42 у=21474836478 - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 4, 'statusMessage': 'Превышены максимальные значения параметров'}
    post_remainder = requests.post(url_remainder, json=low_value)
    print('Результат остатка от деления с числом меньше диапазона х=42 у=-2147483649 - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 4, 'statusMessage': 'Превышены максимальные значения параметров'}
    post_remainder = requests.post(url_remainder, json=fractional_value)
    print('Результат остатка от деления с дробным числом х=42 у=24.5 - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 3, 'statusMessage': 'Значения параметров должны быть целыми'}
    post_remainder = requests.post(url_remainder, json=limit_values)
    print('Результат остатка от деления пограничных чисел х=-2147483648 у=21474836447 - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 4, 'statusMessage': 'Превышены максимальные значения параметров'}
    post_remainder = requests.post(url_remainder, json=underlimit_values)
    print('Результат остатка от деления чисел меньше предела х=-2147483647 у=2147483646 - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 0, 'result': 2147483645}
    post_remainder = requests.post(url_remainder, json=zero_value)
    print('Результат остатка от деления ноль х=42 у=0 - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 8, 'statusMessage': 'Ошибка вычисления'}
    print("Согласно мануалу статус код для ошибки вычисления должен быть 1")

def test_url():
    print('\n\n<<Попытка отправить post-запрос к задаче типа get>>')
    post_remainder = requests.post('http://127.0.0.1:17678/api/state', json=right_values)
    print('\n\nПопытка отправить post-запрос к задаче типа get - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 5, 'statusMessage': ' state - Не верное имя задачи или тип HTTP запроса'}
    post_remainder = requests.get('http://127.0.0.1:17678/api/addition', json=right_values)
    print('Попытка отправить get-запрос к задаче типа post - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 5, 'statusMessage': ': addition - Не верное имя задачи или тип HTTP запроса'}
    post_remainder = requests.get('http://127.0.0.1:17678/api/addition')
    print('Попытка отправить post-запрос без значений  - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 5, 'statusMessage': ': addition - Не верное имя задачи или тип HTTP запроса'}
    post_remainder = requests.get('http://127.0.0.1:17678/api/addition', {'x': 42})
    print('Попытка отправить post-запрос без значения y  - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 5, 'statusMessage': ': addition - Не верное имя задачи или тип HTTP запроса'}

    os.system("webcalculator.exe stop")




