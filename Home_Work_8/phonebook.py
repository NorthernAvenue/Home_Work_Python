import csv
import os


PHONEBOOK_FILE = 'phonebook.txt'
PHONEBOOK_HEADERS = ['Фамилия', 'Имя', 'Отчество', 'Номер телефона']


# Импортирует данные из файла phonebook.txt
def import_phonebook():

    try:
        with open(PHONEBOOK_FILE, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            phonebook = list(reader)
        print('Данные успешно импортированы из файла.')
    except FileNotFoundError:
        phonebook = []
        print('Файл не найден. Создан новый телефонный справочник.')
    return phonebook


# Экспортирует данные из телефонного справочника в файл phonebook.txt
def export_phonebook(phonebook):

    with open(PHONEBOOK_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(phonebook)
    print('Данные успешно экспортированы в файл.')


# Добавляет новую запись в телефонный справочник
def add_contact(phonebook):

    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
# Проверяем корректность введенных данных
    if not all([surname, name, phone]
               ):
        print('Необходимо заполнить фамилию, имя и телефон.')
        return
# Добавляем новую запись в справочник
    phonebook.append([surname, name, patronymic, phone])
    print('Запись успешно добавлена в телефонный справочник.')


# Ищет записи в телефонном справочнике по заданному критерию (фамилия, имя
# или номер телефона)
def search_contact(phonebook):

    search_term = input('Введите фамилию, имя или номер телефона для поиска: ')
    search_results = []
    for contact in phonebook:
        if search_term.lower() in ' '.join(contact).lower():
            search_results.append(contact)
    if search_results:
        print('Найдены следующие записи:')
        for result in search_results:
            print(result)
    else:
        print('Запись не найдена.')


# Выводит все записи в телефонном справочнике
def display_phonebook(phonebook):

    if phonebook:
        for contact in phonebook:
            print(contact)
    else:
        print('Телефонный справочник пуст.')


# Модифицирует запись в телефонном справочнике
def modify_contact(phonebook):

    search_term = input('Введите фамилию, имя или номер телефона для поиска: ')
    search_results = []
    for i, contact in enumerate(phonebook):
        if search_term.lower() in ' '.join(contact).lower():
            search_results.append(i)
    if search_results:
        print(
            f'Найдены следующие записи: {", ".join(str(i+1) for i in search_results)}')
        while True:
            try:
                choice = int(
                    input('Введите номер записи для редактирования: '))
                if choice not in range(1, len(search_results) + 1):
                    raise ValueError
                break
            except ValueError:
                print('Неверный ввод. Попробуйте еще раз.')
        contact = phonebook[search_results[choice - 1]]
        print(f'Редактирование записи: {contact}')
        new_surname = input(
            'Введите новую фамилию (оставьте пустым, чтобы не изменять): ')
        new_name = input(
            'Введите новое имя (оставьте пустым, чтобы не изменять): ')
        new_patronymic = input(
            'Введите новое отчество (оставьте пустым, чтобы не изменять): ')
        new_phone = input(
            'Введите новый номер телефона (оставьте пустым, чтобы не изменять): ')
        if new_surname:
            contact[0] = new_surname
        if new_name:
            contact[1] = new_name
        if new_patronymic:
            contact[2] = new_patronymic
        if new_phone:
            contact[3] = new_phone
        print('Запись успешно изменена.')
    else:
        print('Запись не найдена.')


# Удаление контакта
def delete_contact(phonebook):

    search_term = input('Введите фамилию, имя или номер телефона для поиска: ')
    search_results = []
    for i, contact in enumerate(phonebook):
        if search_term.lower() in ' '.join(contact).lower():
            search_results.append(i)
    if search_results:
        print(
            f'Найдены следующие записи: {", ".join(str(i+1) for i in search_results)}')
        while True:
            try:
                choice = int(input('Введите номер записи для удаления: '))
                if choice not in range(1, len(search_results) + 1):
                    raise ValueError
                break
            except ValueError:
                print('Неверный ввод. Попробуйте еще раз.')
        del phonebook[search_results[choice - 1]]
        print('Запись успешно удалена.')
    else:
        print('Запись не найдена.')


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


print(main())
# if __name__ == "__main__":
#     main()
