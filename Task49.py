# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

file_path = "phonebook.txt"

def show_all_records():
    with open(file_path, "r", encoding="utf-8") as f:
        # records = f.read().split()
        # for i in range(len(records)):
        #     records[i] = records[i].split(";")
        #     print(*records[i])
        for line in f:
            record = line.replace(';',' ')
            print(record, end="") 


def search_record(mode=0):          # 0 - простой поиск, 1 - поиск с возвратом номеров строк(записей)
    print("По каким данным искать?\n"
          "1 - Фамилия\n"
          "2 - Имя\n"
          "3 - Отчество\n"
          "4 - Номер телефона\n")
    select = int(input())
    data = input("Введите данные для поиска: ")
    with open(file_path, "r", encoding="utf-8") as f:        
        num_records = []
        is_find = False
        index = 0
        for line in f:
            if data.lower() in line.split(";")[select - 1].lower():
                if mode == 0:
                    print(line.replace(';',' '), end="")
                elif mode == 1:
                    num_records.append(index)
                is_find = True
            index += 1
        if not is_find:
            print("Нет таких записей")
        elif mode == 1:
            return num_records


def input_data(text: str, endchar=';'):
    data = input(text)
    return(data + endchar)
    

def add_contact():
    new_record = "\n" + input_data('Введите фамилию: ') + input_data("Введите имя: ") + input_data("Введите отчество: ") + input_data("Введите номер телефона: ", "")
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(new_record)

def change_record():
    num_recs = search_record(1)
    index = 0
    temp = ""
    print("Что изменяем?\n"
          "1 - Фамилию\n"
          "2 - Имя\n"
          "3 - Отчество\n"
          "4 - Номер телефона")
    select = int(input())
    data = input("Введите новые данные: ")
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if index in num_recs:
                lst_line = line.split(';')
                lst_line[select - 1] = data
                line = ""
                for i in range(4):                    
                    line += lst_line[i]
                    if i != 3:
                        line += ';'
            temp += line
            index += 1
    with open(file_path, "w",encoding="utf-8") as f:
        f.write(temp)
    

def delete_record():
    num_recs = search_record(1)
    index = 0
    temp = ""
    with open(file_path, "r",encoding="utf-8") as f:
        for line in f:
            if index not in num_recs:
                    temp += line
            index += 1
    with open(file_path, "w",encoding="utf-8") as f:
        f.write(temp)


def main():
    select = 0
    while select != 6:
        print("\n\nВыберите действие:\n"
          "1 - Показать справочник\n"
          "2 - Найти контакт\n"
          "3 - Добавить контакт\n"
          "4 - Изменить контакт\n"
          "5 - Удалить контакт\n"
          "6 - Выход")
        select = int(input())
        if select == 1:
            show_all_records()
        elif select == 2:
            # name = input("Введите фамилию: ")
            search_record()
        elif select == 3:
            add_contact()
        elif select == 4:
            change_record()
        elif select == 5:
            delete_record()

main()
