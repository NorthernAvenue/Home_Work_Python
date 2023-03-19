import csv


PHONEBOOK_FILE = 'phonebook.txt'
PHONEBOOK_HEADERS = ['Фамилия', 'Имя', 'Отчество', 'Номер телефона']

# Экспортирует данные из телефонного справочника в файл phonebook.txt
def export_phonebook(phonebook):

    with open(PHONEBOOK_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(phonebook)
    print('Данные успешно экспортированы в файл.')