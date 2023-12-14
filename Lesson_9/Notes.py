import json
import datetime
import os

path = 'file.txt'


def give_params():
    id = 1
    try:
        with open(path, 'r', encoding='utf-8') as json_file:
            parsed_data = json.load(json_file)
            for note in parsed_data:
                if id < int(note['id']):
                    id = note['id']
            return [id + 1, parsed_data]
    except json.JSONDecodeError as e:
        return [1, []]
    except FileNotFoundError:
        return [1, []]


def prepare_write_note():
    result = give_params()
    note_id = result[0]
    notes = result[1]
    time_stamp = datetime.datetime.today().strftime("%d.%m.%Y %H:%M")
    head = input('-> Введите заголовок: ')
    text = input('-> Введите содержание заметки: ')
    note = {'id': note_id, 'head': head, 'text': text, 'time_stamp': time_stamp}
    notes.append(note)
    write_note(notes)
    print('\n-> Заметка успешно сохранена!\n')
    print(f'id: {note_id}\nhead: {head}\ntext: {text}\ntime_stamp: {time_stamp}\n')


def write_note(data):
    with open(path, 'w', encoding="utf-8") as list:
        list.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ':')))


def give_all_notes():
    try:
        with open(path, 'r', encoding='utf-8') as json_file:
            parsed_data = json.load(json_file)
            return parsed_data
    except json.JSONDecodeError as e:
        return []
    except FileNotFoundError:
        return []


def print_all_notes(notes):
    if len(notes):
        for note in notes:
            print('id: ' + str(note['id']))
            print('head: ' + note['head'])
            print('text: ' + note['text'])
            print('time_stamp: ' + note['time_stamp'] + '\n')
    else:
        print("\n-> Заметок не найдено! \n")


def get_note_index(coincidences, notes):
    index = 1
    my_dict = dict()
    for value in coincidences:
        print(
            f'{index}.id: {value["id"]}\nhead: {value["head"]}\ntext: {value["text"]}\ntime_stamp: {value["time_stamp"]}\n')
        my_dict[index] = [value]
        index += 1
    check_val = index
    my_dict[check_val] = check_val
    message = f'\n-> Введите порядковый номер заметки или --> {check_val} <-- для изменения параметров поиска:\n--> '
    choose = validate_user_input(message, my_dict.keys())

    if choose == check_val:
        while True:
            coincidences = give_find_index(notes)
            print(f'\n<----- Найдено {len(coincidences)} совпадени/е/я/ий ----->\n')
            if len(coincidences) == 1:
                return coincidences
            my_dict[choose] = get_note_index(coincidences, notes)
            break
    return my_dict[choose]


def give_find_index(all_notes):
    find = input('\n-> Введите значение для поиска заметки:\n--> ')
    return find_note(all_notes, find) if (len(find) and len(all_notes)) else []


def no_matches(all_notes, coincidences):
    user_answer = ''
    if len(coincidences) == 0:
        message = '\n-> Введите номер варианта:\n1.Изменить параметры поиска\n2.Выйти в главное меню\n--> '
        answer = validate_user_input(message, [1, 2])
        if answer == 1:
            while True:
                coincidences = give_find_index(all_notes)
                print(f'\n<----- Найдено {len(coincidences)} совпадени/е/я/ий ----->\n')
                if len(coincidences): break
                answer = validate_user_input(message, [1, 2])
                if answer == 2: break
        if answer == 2:
            user_answer = 'main'
    return {'coincidences': coincidences, 'user_answer': user_answer}


def validate_user_input(message, param):
    answer = validateInt(message, "\n-> Вы ввели не число!\n")
    while answer not in param:
        print('\n-> Ошибка, неверный номер!\n')
        answer = int(input(message))
    return answer


def delete_note(note, notes):
    item = note[0]
    print('\n-> Вы точно хотите удалить заметку?\n')
    print(f'id: {item["id"]}\nhead: {item["head"]}\ntext: {item["text"]}\ntime_stamp: {item["time_stamp"]}\n')

    message = '\n-> Введите номер варианта:\n1.Да\n2.Нет\n--> '
    answer = validate_user_input(message, [1, 2])
    if answer == 1:
        if len(notes) > 0:
            for i in range(len(notes)):
                if notes[i]["id"] == int(item["id"]):
                    notes.pop(i)
                    break
            write_note(notes)
            print('\n-> Удаление завершено!\n')


def fill_str(names):
    message = '\n-> Введите номер варианта:'
    for i in range(len(names) + 1):
        if i < len(names):
            message += f"\n{i + 1}.{names[i]}"
        else:
            message += f"\n--> "
    return message


def edit_note(note, notes):
    item = note[0]
    print(f'\n-> Изменение заметки:\n')
    print(f'id: {item["id"]}\nhead: {item["head"]}\ntext: {item["text"]}\ntime_stamp: {item["time_stamp"]}\n')
    names = ['Заголовок', 'Текст']
    message = fill_str(names)
    answer = validate_user_input(message, [i for i in range(1, len(names) + 1)])
    field = ["head", "заголовок"] if answer == 1 else ["text", "текст"]
    old_value = None
    new_value = None
    if len(notes) > 0:
        for i in range(len(notes)):
            if notes[i]["id"] == int(item["id"]):
                old_value = item[field[0]]
                new_value = input(f'\n-> Введите новое значение поля "{field[1]}"\n--> ')
                notes[i][field[0]] = new_value
                notes[i]['time_stamp'] = datetime.datetime.today().strftime("%d.%m.%Y %H:%M")
                break
        write_note(notes)
    print(
        f'\n-> Изменение поля "{field[1]}" прошло успешно!\nСтарое значение: "{old_value}"\nНовое значение: "{new_value}"\n')


def router_func(value):
    note = None
    all_notes = give_all_notes()
    if not len(all_notes):
        return print("\n-> Список заметок пуст!\nСначала создайте заметку\n")
    coincidences = give_find_index(all_notes)
    print(f'\n<----- Найдено {len(coincidences)} совпадени/е/я/ий ----->\n')
    request = no_matches(all_notes, coincidences)
    coincidences = request['coincidences']
    if request['user_answer'] == 'main':
        return initial_func()
    if len(coincidences) == 1:
        note = coincidences
    elif len(coincidences) > 1:
        note = get_note_index(coincidences, all_notes)
    match value:
        case 'delete':
            delete_note(note, all_notes)
        case 'find':
            print('\n-> Искомая заметка:\n')
            print_all_notes(note)
        case 'edit':
            edit_note(note, all_notes)


def find_note(all_notes, find):
    result = [x for x in all_notes if (
                find.lower() in x["head"].lower() or find.lower() in x["text"].lower() or find.lower() in x[
            "time_stamp"].lower())]
    return result


def validateInt(msg, error):
    user_input = input(msg)
    while not user_input.isdigit():
        print(error)
        user_input = input(msg)
    return int(user_input)


def initial_func(state=True):
    str = '-> Введите номер варианта действия с заметками:\n1.Создать\n2.Найти\n3.Изменить\n4.Удалить\n5.Все заметки\n0.Выход\n--> '
    while (state):
        print('\n---> Программа "Менеджер заметок" <---\n')
        command = validateInt(str, '\n-> Вы ввели не число!\n')
        match command:
            case 1:
                print('-----> Раздел - Создание заметки')
                prepare_write_note()
            case 2:
                print('-----> Раздел - Поиск заметки')
                router_func('find')
            case 3:
                print('-----> Раздел - Изменить заметку')
                router_func('edit')
            case 4:
                print('-----> Раздел - Удалить заметку')
                router_func('delete')
            case 5:
                print('-----> Раздел - Все заметки:')
                notes = give_all_notes()
                if not len(notes):
                    print("\nСписок заметок пуст!\nСначала создайте заметку\n")
                else:
                    print_all_notes(notes)
            case 0:
                print('\n<-----> Завершение работы <----->\n')
                return
            case _:
                print('\n-> Неверная команда!\n')


initial_func()
