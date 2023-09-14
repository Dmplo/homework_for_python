# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций.
# Ваша программа не должна быть линейной

path = 'file.txt'

def prepareWriteContact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = validatePhone('Введите телефон: ')
    writeContact(f'{name} {surname} {phone}\n')
    print(f'<----->\n<- Контакт {name} {surname} {phone} успешно содан! ->')

def validatePhone(str):
    phone = input(str)
    while not phone.isdigit():
        print('-> Ошибка, номер телефона должен содержать только цифры!')
        phone = input(str)
    return phone

def writeContact(contact, mode="a"):
    with open('file.txt', mode, encoding="utf-8") as data:
        data.write(contact)

def findCoincidences(find, data, flag=True):
    result = []
    index = 0
    for line in data:
        if find.lower() in line.lower():
            if flag:
                result.append(line)
            else:
                result.append(index)
        index += 1
    return result

def showResults(value):
    if len(value):
        for i in value:
            print(i, end='')
    else: print('<----->\nСписок контактов пуст!')

def giveAllContacts():
    result = []
    with open('file.txt', 'r', encoding="utf-8") as data:
        for line in data:
            result.append(line)
    return result

def getContactIndex(coincidences, all_contacts):
    index = 1
    my_dict = dict()
    for value in coincidences:
        print(f'{index}.{all_contacts[value][:-1]}')
        my_dict[index] = value
        index += 1
    check_val = coincidences[len(coincidences) - 1] + 1
    my_dict[check_val] = check_val
    message = f'<----->\nВведите порядковый номер контакта или --> {check_val} <-- для изменения параметров поиска:\n--> '
    choose = validateUserInput(message, my_dict.keys())
    return None if choose == check_val else my_dict[choose]

def giveFindIndex(all_contacts):
        find = input('<----->\nВведите значение для поиска контакта:\n--> ')
        return findCoincidences(find, all_contacts, False) if len(find) else []

def noMatches(all_contacts, coincidences):
    user_answer = ''
    if len(coincidences) == 0:
        message = '<----->\nВведите номер варианта:\n1.Изменить параметры поиска\n2.Выйти в главное меню\n--> '
        answer = validateUserInput(message, [1, 2])
        if answer == 1:
            while True:
                coincidences = giveFindIndex(all_contacts)
                print(f'<----->\n<----- Найдено {len(coincidences)} совпадени/е/я/ий ----->')
                if len(coincidences): break
                answer = validateUserInput(message, [1, 2])
                if answer == 2: break
        if answer == 2:
            user_answer = 'main' 
    return {'coincidences': coincidences, 'user_answer': user_answer}  

def writeChanges(all_contacts):
    if len(all_contacts):
        for index in range(len(all_contacts)):
            match index:
                case 0:
                    writeContact(all_contacts[index], 'w')
                case _:
                    writeContact(all_contacts[index])
    else:
        with open('file.txt', 'w', encoding="utf-8") as data:
            data.write('')

def validateUserInput(message, param):
    answer = int(input(message))
    while answer not in param:
        print('-> Ошибка, неверный номер!')
        answer = int(input(message))
    return answer

def isEndProgram():
    message = '<----->\nВыберите дальнейшее действие, введите номер варианта:\n1.Выйти из программы\n2.В главное меню\n--> '
    result = validateUserInput(message, [1, 2])
    if result == 2: initialFunc()
    else: print('<----->\nЗавершение работы\n<----->')


def deleteContact(all_contacts, choose_index):
    print(f'<----->\nВы точно хотите удалить --> {all_contacts[choose_index][:-1]} <-- ?')
    message = 'Введите номер варианта:\n1.Да\n2.Нет\n--> '
    answer = validateUserInput(message, [1, 2])
    if answer == 1:
        deleted_contact = all_contacts.pop(choose_index)
        writeChanges(all_contacts)      
        print(f'<----->\n<- Удаление {deleted_contact[:-1]} успешно завершено! ->')

def fillStr(names):
    message = 'Введите номер варианта:'
    for i in range(len(names) + 1):
        if i < len(names):
            message += f"\n{i + 1}.{names[i]}"
        else: 
            message += f"\n--> "
    return message

def editContact(all_contacts, choose_index):
    change_field = None
    print(f'Изменение контакта --> {all_contacts[choose_index][:-1]} <--')
    names = ['Имя', 'Фамилия', 'Телефон']
    message = fillStr(names)
    answer = validateUserInput(message, [i for i in range(1, len(names) + 1)])
    field = all_contacts[choose_index].split(' ')
    old_field = field[answer - 1]
    check_field = names[answer - 1].lower() == 'телефон'
    if check_field:
        str = f'Введите новое значение поля "{names[answer - 1]}"\n--> '
        change_field = f"{validatePhone(str)}\n"
    else: change_field = input(f'Введите новое значение поля "{names[answer - 1]}"\n--> ')
    field[answer - 1] = change_field
    all_contacts[choose_index] = ' '. join (field)
    writeChanges(all_contacts)      
    print(f'<----->\n<- Изменение поля "{names[answer - 1]}" прошло успешно! ->\nСтарое значение: "{old_field[:-1] if check_field else old_field}", новое значение: "{change_field[:-1] if check_field else change_field}"\nРезультат: {all_contacts[choose_index][:-1]}')

def routerFunc(value, number):
    choose_index = None
    all_contacts = giveAllContacts()
    coincidences = giveFindIndex(all_contacts)
    print(f'<----->\n<----- Найдено {len(coincidences)} совпадени/е/я/ий ----->')
    request = noMatches(all_contacts, coincidences)
    coincidences = request['coincidences']
    if request['user_answer'] == 'main':          
        return initialFunc()
    if len(coincidences) == 1:
        choose_index = coincidences[0]
    elif len(coincidences) > 1:
        choose_index = getContactIndex(coincidences, all_contacts)
    if choose_index is None:
            return initialFunc(number) 
    
    match value:
        case 'delete':
            deleteContact(all_contacts, choose_index)
        case 'find':
            print(f'Искомый контакт --> {all_contacts[choose_index][:-1]} <-- ')
        case 'edit':
            editContact(all_contacts, choose_index)
    
    isEndProgram()

def initialFunc(rec_command=None):
    if rec_command is None:
        print('---> Программа "телефоный справочник" <---')    
    str = 'Введите номер варианта действия с контактами:\n1.Создать\n2.Найти\n3.Изменить\n4.Удалить\n5.Все контакты\n--> '
    command = int(input(str)) if rec_command is None else rec_command
    match command:
        case 1:
            print('-----> Раздел - Создание контакта')
            prepareWriteContact()
            isEndProgram()
        case 2:
            print('-----> Раздел - Поиск контакта')
            routerFunc('find', 2)
        case 3:
            print('-----> Раздел - Изменить контакт')
            routerFunc('edit', 3)
        case 4:
            print('-----> Раздел - Удалить контакт')
            routerFunc('delete', 4)
        case 5:
            print('-----> Раздел - Все контакты:')
            showResults(giveAllContacts())
            isEndProgram()
        case _:
            print('Not found')

initialFunc()
