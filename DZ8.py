'''Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной '''

# Меню программы
def menu():
    while True:
        print('Выберите нужный пункт')
        user_choice = input(' 1 - Добавить контакт \n 2 - Найти контакт \n 3 - Изменить контакт \n 4 - Удалить контакт \n 5 - Импортировать данные \n 6 - Экспортировать данные \n 7 - Посмотреть все контакты \n 8 - выйти из приложения \n >>> ')
        if user_choice == '1':
            add_contact()
        elif user_choice == '2':
            contact_list = contacts(phonebook)
            find_contact(contact_list)         
        elif user_choice == '3':
            modification_contacts(phonebook)
        elif user_choice == '4':
            print('В разработке')
        elif user_choice == '5':
            print('В разработке')
        elif user_choice == '6':
            print('В разработке')
        elif user_choice == '7':
            get_full_contact(phonebook)
        elif user_choice == '8':
            print('До свидания!')
            exit()
        else:
            print('Неправильно выбрана команда! \n')

# Добавление контакта
def add_contact():
    data = [
        input('Введите фамилию: '),
        input('Введите имя: '),
        input('Введите отчество: '),
        input('Введите номер телефона: '),
    ]
    line = ' '.join(data)
    with open(phonebook, 'a', encoding='utf-8') as file:
        file.write(line + '\n')
        print(f'Контакт {data[0]} {data[1]} {data[2]} добавлен!') 
    return

# Просмотр всех контактов
def get_full_contact(phonebook):
    with open(phonebook, 'r', encoding='utf-8') as phonebook:
        data = phonebook.readlines()
    headers = ['Фамилия', 'Имя', 'Отчество', 'Номер телефона']
    print('\t\t'.join(headers))
    for line in data:
        print('\t\t'.join(line.split(' ')))
        
# Формирование списка ключ <-> значение    
def contacts(phonebook):
    with open(phonebook, 'r', encoding='utf-8') as phonebook:
        data = phonebook.readlines()
    headers = ['Фамилия', 'Имя', 'Отчество', 'Номер телефона']
    contact_list = []
    for line in data:
        line = line.split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list

# Поиск контакта по параметрам
def search_parameters():
    while True:
        search = input('Поиск по\n 1 - фамилии \n 2 - имени \n 3 - отчеству \n 4 - номеру телефона \n >>> ')
        search_value = None
        if search == '1':
            search_value = input('Введите фамилию для поиска: ')
            return search, search_value
        elif search == '2':
            search_value = input('Введите имя для поиска: ')
            return search, search_value
        elif search == '3':
            search_value = input('Введите отчество для поиска: ')
            return search, search_value
        elif search == '4':
            search_value = input('Введите номер телефона для поиска: ')
            return search, search_value
        else:
            print('Неправильно выбрана команда! \n')

# Вывод контакта из phonebook.txt
def find_contact(contact_list):
    search, search_value = search_parameters()    
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Отчество', '4': 'Номер телефона'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)

# Вывод информации по контакту
def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}:{value:12}', end='\n')
        print()

# Изменение контакта
def modification_contacts(phonebook):
    contact_list = contacts(phonebook)
    contact_to_change = search_modification_contact(contact_list) 
    contact_list.remove(contact_to_change)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n>>>')
    if field == '1':
        contact_to_change[0] = input('Введите фамилию: ')
    elif field == '2':
        contact_to_change[1] = input('Введите имя: ')
    elif field == '3':
        contact_to_change[2] = input('Введите номер телефона: ')
    contact_list.append(contact_to_change)
    with open(phonebook, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)
            
# Поиск контакта для исправления
def search_modification_contact(contact_list: list):
    search, search_value = search_parameters()
    list_result = []
    for contact in contact_list:
        for values in contact.values():
            if values == search_value:
                list_result.append(contact)
    if len(list_result) == 1:
        return list_result[0]
    elif len(list_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(list_result)):
            print(f'{i + 1} - {list_result[i]}')
        num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
        return list_result[num_count - 1]
    else:
        print('Контакт не найден')
        menu(3)
    

phonebook = 'phonebook.txt' 
menu()