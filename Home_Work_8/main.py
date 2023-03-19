import csv
from modules.add_contact_module import add_contact
from modules.delete_contact_module import delete_contact
from modules.display_phone_module import display_phonebook
from modules.export_module import export_phonebook
from modules.import_module import import_phonebook
from modules.modify_contact_module import modify_contact
from modules.search_contact_module import search_contact


# Основная программа
def main():
    phonebook = import_phonebook()
    while True:
        print('Меню:')
        print('1. Вывести все записи в телефонном справочнике')
        print('2. Добавить новую запись')
        print('3. Поиск записи по фамилии, имени или номеру телефона')
        print('4. Изменить запись в телефонном справочнике')
        print('5. Удалить запись из телефонного справочника')
        print('6. Экспортировать данные в файл')
        print('7. Выход из программы')
        choice = input('Введите номер выбранного действия: ')
        if choice == '1':
            display_phonebook(phonebook)
        elif choice == '2':
            add_contact(phonebook)
        elif choice == '3':
            search_contact(phonebook)
        elif choice == '4':
            modify_contact(phonebook)
        elif choice == '5':
            delete_contact(phonebook)
        elif choice == '6':
            export_phonebook(phonebook)
        elif choice == '7':
            break
        else:
            print('Неверный ввод. Попробуйте еще раз.')
    print('До свидания!')


if __name__ == "__main__":
    main()
