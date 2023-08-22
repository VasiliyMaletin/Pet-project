import phone_book


def user_choice():  # Основное меню приложения
    menu_item = int(input('\n1 - Постраничный вывод записей\n2 - Добавление новой записи\n3 - Редактирование записи'
                          '\n4 - Поиск записи\n5 - Выход\nВыберите пункт меню: '))
    match menu_item:
        case 1:
            print('\nСписок контактов:')
            phone_book.show_book()
        case 2:
            phone_book.add_entry()
        case 3:
            phone_book.edit_entry()
        case 4:
            phone_book.search_entry()
        case 5:
            print('\nСпасибо что пользовались нашим приложением!\nДо новых встреч!')
            exit()
        case _:
            print('\nОшибка ввода!\n\nЧисло должно соответствовать пункту меню!\n')


if __name__ == '__main__':
    user_choice()
