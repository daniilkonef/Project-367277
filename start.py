from datamodel_pack.database_class import CreateDatabaseMachine
from presenter_pack.presenter_class import CreatePresenterObject


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
              "1 - Показать все заметки в книге ;  \n"
              "2 - Показать заметку с номером ID;  \n"
              "3 - Показать заметки имеющие дату;  \n"
              "4 - Добавить новую заметку в книгу; \n"
              "5 - Удалить заметку по номеру ID; \n"
              "6 - Изменить заметку по номеру ID; \n\n"
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
            user_gave_us_a_number = str(input())
            database_machine.print_note_by_date(user_gave_us_a_number)

        if user_selected_is == 4:
            database_machine.handler4()

        if user_selected_is == 5:
            database_machine.handler5()

        if user_selected_is == 6:
            database_machine.handler6()

        presenter.show_empty_lines(10)


main()
