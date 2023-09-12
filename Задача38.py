from core import find_record_in
from core import delete_existing_contact_from
from core import change_existing_contact_from

file_database: str = "database.txt"


def show_all_contacts():
    memory = list()
    with (open(file_database, 'r', encoding="utf-8")) as db:
        for line in db:
            data = line.replace(";", " ")
            memory.append(line.strip())
            print(data, end="")


def get_size_of_database():
    memory = list()
    with (open(file_database, 'r', encoding="utf-8")) as db:
        for line in db:
            memory.append(line.strip())
    # print()
    # print(len(memory))
    return len(memory)


def get_virtual_database() -> list:
    memory = list()
    with (open(file_database, 'r', encoding="utf-8")) as db:
        for line in db:
            memory.append(line.strip())
    return memory


def add_new_contact():
    id_number = get_size_of_database() + 1

    firstname = input("Введите Имя: ") or " - "
    last_name = input("Введите Фамилию: ") or " - "
    patronymic = input("Введите Отчество: ") or " - "
    phone_number = input("Введите номер телефона: ") or " - "
    splitter = str(";")
    new_record = str(
        id_number) + splitter + firstname.strip() + splitter + last_name.strip() + splitter + patronymic.strip() + splitter + phone_number.strip()
    with open(file_database, "a", encoding="utf-8") as db:
        db.write(new_record + "\n")


def main():
    print(get_virtual_database())

    print("ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    print("Выберите действие: \n"
          "1 - Показать все контакты; \n"
          "2 - Найти контакт; \n"
          "3 - Добавить контакт: \n"
          "4 - Удалить контакт: \n"
          "5 - Изменить контакт: \n"
          "Введите цифру и нажмите Enter: ")

    user_selected_is = int(input())
    if user_selected_is == 1:
        show_all_contacts()

    if user_selected_is == 2:
        flag_found = find_record_in(get_virtual_database(), str(input("Введите что ищем: ")))
        if flag_found == False:
            print("По вашему запросу нет информации в базе.")

    if user_selected_is == 3:
        add_new_contact()

    if user_selected_is == 4:
        delete_existing_contact_from(file_database)

    if user_selected_is == 5:
        change_existing_contact_from(file_database)

main()
