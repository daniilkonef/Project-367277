# database = ['1;Конев;Дан;Ник;+7984156584654',
#             '2;Ивано;Иван;Никол;+7968165215',
#             '3;Ингви;Джей;Мальмстин;+198652338',
#             '4;Брайян;Джонсон;ACDC;+198652338',
#             '5;Джо;Ди;Майо;+16916988484']
# #
# #
# print(len(database))


def find_record_in(database, what_im_looking_for: str):
    flag_found: bool = False
    for index in range(len(database)):
        one_record = database[index].split(";")
        id_number = (int(one_record[0]))
        last_name = (str(one_record[1]))
        first_name = (str(one_record[2]))
        patronymic = (str(one_record[3]))
        phone_num = (str(one_record[4]))

        if what_im_looking_for in one_record:
            # print(one_record)
            flag_found = True
            print(
                f"ID: {id_number}, \t Фамилия: {last_name}, \tИмя: {first_name}, \t Отчество: {patronymic}, \t\tТелефон: {phone_num};")
    return flag_found


# find_record_in(database, "Конев")
# find_record_in(database, "Ивано")
# find_record_in(database, "Ингви")


def delete_existing_contact_from(file_database):
    id_number = int(input("Введите ID номер записи для ее удаления: "))
    memory = list()
    with (open(file_database, 'r', encoding="utf-8")) as db:
        for line in db:
            memory.append(line.strip())
    print(f"Был удален контакт: {memory.pop(id_number - 1)}")
    # print(memory)

    f = open(file_database, 'w+')
    f.seek(0)
    f.close()

    for index in range(len(memory)):
        one_record = memory[index].split(";")
        id_number = int(index) + 1
        last_name = (str(one_record[1]))
        first_name = (str(one_record[2]))
        patronymic = (str(one_record[3]))
        phone_num = (str(one_record[4]))
        splitter = str(";")
        new_record = str(id_number) + splitter + first_name.strip() + splitter + last_name.strip() + splitter + patronymic.strip() + splitter + phone_num.strip()
        print(new_record)

        with open(file_database, "a", encoding="utf-8") as handle:
            handle.write(new_record + "\n")


def change_existing_contact_from(file_database):
    id_number = int(input("Введите ID номер записи для ее изменения: "))
    memory = list()
    with (open(file_database, 'r', encoding="utf-8")) as db:
        for line in db:
            memory.append(line.strip())
    # print(memory)

    f = open(file_database, 'w+')
    f.seek(0)
    f.close()

    firstname = input("Введите новое имя: ") or " - "
    last_name = input("Введите новую фамилию: ") or " - "
    patronymic = input("Введите новое отчество: ") or " - "
    phone_number = input("Введите новый номер телефона: ") or " - "
    splitter = str(";")
    new_record = str(id_number) + splitter + firstname.strip() + splitter + last_name.strip() + splitter + patronymic.strip() + splitter + phone_number.strip()
    memory[id_number - 1] = new_record

    # print(memory)

    with open(file_database, "a", encoding="utf-8") as db:
        for my_str in memory:
            print(my_str)
            db.write(my_str + "\n")

