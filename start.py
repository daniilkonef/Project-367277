import os

from core import find_record_in
from core import delete_existing_contact_from
from core import change_existing_contact_from

from datamodel_pack.database_class import CreateDatabaseMachine
from presenter_pack.presenter_class import CreatePresenterObject


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
    database_path = str("datamodel_pack/database_file.json")
    database_machine = CreateDatabaseMachine(database_path)

    print()
    print("ЗАПИСНАЯ КНИГА")
    print("Посмотрите последние 3 записи:")
    presenter = CreatePresenterObject(database_machine)
    presenter.show_3_last_notes()

    while True:
        print()
        print("Выберите действие вводом цифры: \n"
              "1 - Показать все записи в книге ; [+]\n"
              "2 - Показать запись с номером ID; [+]\n"
              "3 - Показать записи имеющие дату; \n"
              "4 - Добавить новую запись в книгу; \n"
              "5 - Редактировать запись по номеру ID; \n"
              "6 - Удалить запись по номеру ID; \n\n"
              ">> ", end=" ")



        user_selected_is = int(input())
        print()
        if user_selected_is == 1:
            presenter.show_all_notes()

        if user_selected_is == 2:
            print("Введите интересующий номер ID: ")
            print(">> ", end="")
            user_gave_us_a_number = int(input())
            database_machine.print_note_by_id(user_gave_us_a_number)
            # flag_found = find_record_in(get_virtual_database(), str(input("Введите что ищем: ")))
            # if flag_found == False:
            #     print("По вашему запросу нет информации в базе.")

        if user_selected_is == 3:
            print("Введите дату в следующем формате: YYYY-MM-DD >> ", end="")
            input()
            # add_new_contact()

        if user_selected_is == 4:
            delete_existing_contact_from(file_database)

        if user_selected_is == 5:
            change_existing_contact_from(file_database)

        presenter.show_empty_lines(10)


main()
