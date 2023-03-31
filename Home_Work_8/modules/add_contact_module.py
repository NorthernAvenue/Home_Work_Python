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
