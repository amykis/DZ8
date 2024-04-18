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
            print('В разработке')
        elif user_choice == '3':
            print('В разработке')
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
            
phonebook = 'phonebook.txt' 
menu()