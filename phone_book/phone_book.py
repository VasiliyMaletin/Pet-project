import controller
import json


def create_data_base():  # Создание файла с базой данных
    data_base = []
    with open('data_base.json', 'w', encoding='utf-8') as db:
        db.write(json.dumps(data_base, indent=2, ensure_ascii=False))
    controller.user_choice()


def show_book():  # Вывод базы данных в консоль
    with open('data_base.json', encoding='UTF-8') as db:
        data = json.load(db)
    for i in range(0, len(data)):
        print(print_entry(data, i))
    controller.user_choice()


def print_entry(data, id_entry):  # Функция форматирования вывода в консоль
    return (f'\nЗапись №{data[id_entry]["id"]}:\n'
            f'{data[id_entry]["Surname"] + " " + data[id_entry]["Name"] + " " + data[id_entry]["Patronymic"]}\n'
            f'Название организации: {data[id_entry]["Organization"]}\n'
            f'Рабочий номер телефона: {data[id_entry]["Work phone number"]}\n'
            f'Личный номер телефона: {data[id_entry]["Personal phone number"]}')


def add_entry():  # Функция добавления записи
    id_entry = 1
    surname = input('\nВведите Фамилию: ')
    name = input('Введите Имя: ')
    patronymic = input('Введите Отчество: ')
    organization = input('Введите название организации: ')
    work_phone_number = input('Введите рабочий номер телефона: ')
    personal_phone_number = input('Введите личный номер телефона: ')
    data_base = {
        'id': id_entry,
        'Surname': surname,
        'Name': name,
        'Patronymic': patronymic,
        'Organization': organization,
        'Work phone number': work_phone_number,
        "Personal phone number": personal_phone_number,
    }
    with open('data_base.json', encoding='utf-8') as db:
        data = json.load(db)
    tmp_id = []
    for i in range(len(data)):
        tmp_id.append(data[i]['id'])
    if data_base['id'] not in tmp_id:
        data.append(data_base)
    else:
        max_id = max(tmp_id)
        data_base['id'] = max_id + 1
        data.append(data_base)
    with open('data_base.json', 'w', encoding='utf-8') as db:
        json.dump(data, db, indent=2, ensure_ascii=False)
    controller.user_choice()
    return '\nНовый контакт успешно добавлен!\n'


def edit_entry():  # Функция редактирования записи
    id_entry = int(input('\nВведите номер записи для редактирования: '))

    with open('data_base.json', encoding='UTF-8') as db:
        data = json.load(db)
        flag = False
        for i in range(len(data)):
            if id_entry == data[i]['id']:
                flag = True
                menu_item = int(input(
                    '\n1 - Фамилию\n2 - Имя\n3 - Отчество\n4 - Организацию\n5 - Рабочий номер телефона\n'
                    '6 - Личный номер телефона\nВыберите что хотите изменить: '))
                match menu_item:
                    case 1:
                        data[i]['Surname'] = input('\nВведите Фамилию: ')
                    case 2:
                        data[i]['Name'] = input('\nВведите Имя: ')
                    case 3:
                        data[i]['Patronymic'] = input('\nВведите Отчество: ')
                    case 4:
                        data[i]['Organization'] = input('\nВведите название организации: ')
                    case 5:
                        data[i]['Work phone number'] = input('\nВведите рабочий номер телефона: ')
                    case 6:
                        data[i]['Personal phone number'] = input('\nВведите личный номер телефона: ')
                with open('data_base.json', 'w', encoding='UTF-8') as db:
                    json.dump(data, db, indent=2, ensure_ascii=False)
                print('\nЗапись успешно изменена!')
                break
        if not flag:
            print('\nЗаписи с таким номером не существует!')
    controller.user_choice()


def search_entry():  # Функция поиска по заданным параметрам
    with open('data_base.json', encoding='UTF-8') as db:
        data = json.load(db)
    menu_item = int(input(
        '\n1 - Фамилия\n2 - Имя\n3 - Отчество\n4 - Организация\n5 - Рабочий номер телефона\n'
        '6 - Личный номер телефона\n7 - По нескольким параметрам\nВыберите по какому параметру искать: '))
    match menu_item:
        case 1:
            find_entry = input('\nВведите Фамилию: ')
            find(data, 'Surname', find_entry)
        case 2:
            find_entry = input('\nВведите Имя: ')
            find(data, 'Name', find_entry)
        case 3:
            find_entry = input('\nВведите Отчество: ')
            find(data, 'Patronymic', find_entry)
        case 4:
            find_entry = input('\nВведите название организации: ')
            find(data, 'Organization', find_entry)
        case 5:
            find_entry = input('\nВведите рабочий номер телефона: ')
            find(data, 'Work phone number', find_entry)
        case 6:
            find_entry = input('\nВведите личный номер телефона: ')
            find(data, 'Personal phone number', find_entry)
        case 7:
            pass
    controller.user_choice()


def find(data, search_param, find_entry):  # Функция вывода поиска записи по заданным параметрам
    for i in range(len(data)):
        if find_entry == data[i][search_param]:
            print(print_entry(data, i))
    return


def remove_entry():  # Функция удаления записи
    pass


if __name__ == '__main__':
    show_book()
