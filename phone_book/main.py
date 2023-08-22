from controller import user_choice
from phone_book import create_data_base
from os import path


if not path.exists('data_base.json'):
    create_data_base()

print('Добро пожаловать в наше приложение!')
user_choice()
