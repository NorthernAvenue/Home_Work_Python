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