# Выводит все записи в телефонном справочнике
def display_phonebook(phonebook):

    if phonebook:
        for contact in phonebook:
            print(contact)
    else:
        print('Телефонный справочник пуст.')
