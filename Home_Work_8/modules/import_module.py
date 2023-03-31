import csv


# Импортирует данные из файла phonebook.txt
PHONEBOOK_FILE = 'phonebook.txt'
PHONEBOOK_HEADERS = ['Фамилия', 'Имя', 'Отчество', 'Номер телефона']


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
