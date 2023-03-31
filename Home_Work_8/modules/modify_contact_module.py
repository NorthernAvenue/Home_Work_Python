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
