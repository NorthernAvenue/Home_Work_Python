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
