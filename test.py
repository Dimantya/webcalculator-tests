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
    print('\n\n<<�������� �������, ��������� � �������� ���������� webcalculator.exe>>')
    print('\n\n<����� �� ����������� ������ � ����� 127.0.0.1:17678>')
    os.system("webcalculator.exe start")
    print('\n\n<������� ���������� ������ ��� ��� ���������� ����������>')
    os.system("webcalculator.exe start")
    print('\n\n<���������� ������ ����������, �������� ���������� ������ � ����� � �������� �������: 127.0.0.1:17678>')
    os.system("webcalculator.exe restart")
    print('\n\n<��������� ������ ����������>')
    os.system("webcalculator.exe stop")
    print('\n\n<����� �� ����������� ������ 127.0.0.1 � ����� 5413>')
    os.system("webcalculator.exe start localhost 5413")
    print('\n\n<���������� ������ ����������, �������� ���������� ������ � ����� � �������� �������: 127.0.0.1: 5413>')
    os.system("webcalculator.exe restart")
    print('\n\n<��������� ������ ����������>')
    os.system("webcalculator.exe stop")
    print('\n\n<����� ���������� �� ������ 127.2.5.10 � ����� 5413>')
    os.system("webcalculator.exe start 127.2.5.10 5413")
    print('\n\n<���������� ������ ����������, �������� ���������� ������ � ����� � �������� �������: 127.2.5.10 � ����� 5413>')
    os.system("webcalculator.exe restart")
    print('\n\n<��������� ������ ����������>')
    os.system("webcalculator.exe stop")

def test_get():
    print('\n\n<<�������� get-������� � ������� �������>>')
    os.system("webcalculator.exe start")
    get_response = requests.get(url_get)
    print('\n\n��������� �������: ', get_response.json())
    assert get_response.json() == {'statusCode': 0, 'state': 'O�'}


def test_addition():
    print('\n\n<<�������� post-������� ��� �������� ��������>>')
    post_addition = requests.post(url_addition, json=right_values)
    print('\n\n��������� �������� � ����������� ���������� �=42 �=24 - ', post_addition.json())
    assert post_addition.json() == {'statusCode': 0, 'result': 66}
    post_addition = requests.post(url_addition, json=high_value)
    print('��������� �������� � ������ ������ ��������� �=42 �=21474836478 - ', post_addition.json())
    assert post_addition.json() == {'statusCode': 4, 'statusMessage': '��������� ������������ �������� ����������'}
    post_addition = requests.post(url_addition, json=low_value)
    print('��������� �������� � ������ ������ ��������� �=42 �=-2147483649 - ', post_addition.json())
    assert post_addition.json() == {'statusCode': 4, 'statusMessage': '��������� ������������ �������� ����������'}
    post_addition = requests.post(url_addition, json=fractional_value)
    print('��������� �������� � ������� ������ �=42 �=24.5 - ', post_addition.json())
    assert post_addition.json() == {'statusCode': 3, 'statusMessage': '�������� ���������� ������ ���� ������'}
    post_addition = requests.post(url_addition, json=limit_values)
    print('��������� �������� ����������� ����� �=-2147483648 �=21474836447 - ', post_addition.json())
    assert post_addition.json() == {'statusCode': 4, 'statusMessage': '��������� ������������ �������� ����������'}
    post_addition = requests.post(url_addition, json=underlimit_values)
    print('��������� �������� ����� ������ ������� �=-2147483647 �=2147483646 - ', post_addition.json())
    assert post_addition.json() == {'statusCode': 0, 'result': -1}

def test_multiplication():
    print('\n\n<<�������� post-������� ��� �������� ���������>>')
    post_multiplication = requests.post(url_multiplication, json=right_values)
    print('\n\n��������� ��������� � ����������� ���������� �=42 �=24 - ', post_multiplication.json())
    assert post_multiplication.json() == {'statusCode': 0, 'result': 1008}
    post_multiplication = requests.post(url_multiplication, json=high_value)
    print('��������� ��������� � ������ ������ ��������� �=42 �=21474836478 - ', post_multiplication.json())
    assert post_multiplication.json() == {'statusCode': 4, 'statusMessage': '��������� ������������ �������� ����������'}
    post_multiplication = requests.post(url_addition, json=low_value)
    print('��������� ��������� � ������ ������ ��������� �=42 �=-2147483649 - ', post_multiplication.json())
    assert post_multiplication.json() == {'statusCode': 4, 'statusMessage': '��������� ������������ �������� ����������'}
    post_multiplication = requests.post(url_multiplication, json=fractional_value)
    print('��������� ��������� � ������� ������ �=42 �=24.5 - ', post_multiplication.json())
    assert post_multiplication.json() == {'statusCode': 3, 'statusMessage': '�������� ���������� ������ ���� ������'}
    post_multiplication = requests.post(url_multiplication, json=limit_values)
    print('��������� ��������� ����������� ����� �=-2147483648 �=21474836447 - ', post_multiplication.json())
    assert post_multiplication.json() == {'statusCode': 4, 'statusMessage': '��������� ������������ �������� ����������'}
    post_multiplication = requests.post(url_multiplication, json=underlimit_values)
    print('��������� ��������� ����� ������ ������� - ', post_multiplication.json())
    assert post_multiplication.json() == {'statusCode': 0, 'result': -4611686011984936962}


def test_division():
    print('\n\n<<�������� post-������� ��� �������� �������>>')
    post_division = requests.post(url_division, json=right_values)
    print('\n\n��������� ������� � ����������� ���������� �=42 �=24 - ', post_division.json())
    assert post_division.json() == {'statusCode': 0, 'result': 1}
    post_division = requests.post(url_division, json=high_value)
    print('��������� ������� � ������ ������ ��������� �=42 �=21474836478 - ', post_division.json())
    assert post_division.json() == {'statusCode': 4, 'statusMessage': '��������� ������������ �������� ����������'}
    post_division = requests.post(url_division, json=low_value)
    print('��������� ������� � ������ ������ ��������� �=42 �=-2147483649 - ', post_division.json())
    assert post_division.json() == {'statusCode': 4, 'statusMessage': '��������� ������������ �������� ����������'}
    post_division = requests.post(url_division, json=fractional_value)
    print('��������� ������� � ������� ������ �=42 �=24.5 - ', post_division.json())
    assert post_division.json() == {'statusCode': 3, 'statusMessage': '�������� ���������� ������ ���� ������'}
    post_division = requests.post(url_division, json=limit_values)
    print('��������� ������� ����������� ����� �=-2147483648 �=21474836447 - ', post_division.json())
    assert post_division.json() == {'statusCode': 4, 'statusMessage': '��������� ������������ �������� ����������'}
    post_division = requests.post(url_division, json=underlimit_values)
    print('��������� ������� ����� ������ ������� �=-2147483647 �=2147483646 - ', post_division.json())
    assert post_division.json() == {'statusCode': 0, 'result': -2}
    post_division = requests.post(url_division, json=zero_value)
    print('��������� ������� ���� �=42 �=0 - ', post_division.json())
    assert post_division.json() == {'statusCode': 8, 'statusMessage': '������ ����������'}

def test_remainder():
    print('\n\n<<�������� post-������� ��� �������� ������� �� �������>>')
    post_remainder = requests.post(url_remainder, json=right_values)
    print('\n\n��������� ������� �� ������� � ����������� ���������� �=42 �=24 - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 0, 'result': 18}
    post_remainder = requests.post(url_division, json=high_value)
    print('��������� ������� �� ������� � ������ ������ ��������� �=42 �=21474836478 - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 4, 'statusMessage': '��������� ������������ �������� ����������'}
    post_remainder = requests.post(url_remainder, json=low_value)
    print('��������� ������� �� ������� � ������ ������ ��������� �=42 �=-2147483649 - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 4, 'statusMessage': '��������� ������������ �������� ����������'}
    post_remainder = requests.post(url_remainder, json=fractional_value)
    print('��������� ������� �� ������� � ������� ������ �=42 �=24.5 - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 3, 'statusMessage': '�������� ���������� ������ ���� ������'}
    post_remainder = requests.post(url_remainder, json=limit_values)
    print('��������� ������� �� ������� ����������� ����� �=-2147483648 �=21474836447 - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 4, 'statusMessage': '��������� ������������ �������� ����������'}
    post_remainder = requests.post(url_remainder, json=underlimit_values)
    print('��������� ������� �� ������� ����� ������ ������� �=-2147483647 �=2147483646 - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 0, 'result': 2147483645}
    post_remainder = requests.post(url_remainder, json=zero_value)
    print('��������� ������� �� ������� ���� �=42 �=0 - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 8, 'statusMessage': '������ ����������'}
    print("�������� ������� ������ ��� ��� ������ ���������� ������ ���� 1")

def test_url():
    print('\n\n<<������� ��������� post-������ � ������ ���� get>>')
    post_remainder = requests.post('http://127.0.0.1:17678/api/state', json=right_values)
    print('\n\n������� ��������� post-������ � ������ ���� get - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 5, 'statusMessage': ' state - �� ������ ��� ������ ��� ��� HTTP �������'}
    post_remainder = requests.get('http://127.0.0.1:17678/api/addition', json=right_values)
    print('������� ��������� get-������ � ������ ���� post - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 5, 'statusMessage': ': addition - �� ������ ��� ������ ��� ��� HTTP �������'}
    post_remainder = requests.get('http://127.0.0.1:17678/api/addition')
    print('������� ��������� post-������ ��� ��������  - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 5, 'statusMessage': ': addition - �� ������ ��� ������ ��� ��� HTTP �������'}
    post_remainder = requests.get('http://127.0.0.1:17678/api/addition', {'x': 42})
    print('������� ��������� post-������ ��� �������� y  - ', post_remainder.json())
    assert post_remainder.json() == {'statusCode': 5, 'statusMessage': ': addition - �� ������ ��� ������ ��� ��� HTTP �������'}

    os.system("webcalculator.exe stop")




