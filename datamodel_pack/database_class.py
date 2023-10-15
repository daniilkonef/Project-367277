import json
from datetime import datetime


class CreateDatabaseMachine:
    database_in_memory = list()
    file_name_json = str()

    def __init__(self, file_name_json: str):
        self.file_name_json = file_name_json

    def import_database_from(self, file_name_json: str):
        with open(file_name_json, "r", encoding="utf-8") as my_json_file:
            self.database_in_memory = json.load(my_json_file)

    def print_all_notes(self):
        self.import_database_from(self.file_name_json)
        for note_item in self.database_in_memory:
            self.print_one_note_beautyfully(note_item)

    def print_note_by_id(self, note_id: int):
        self.import_database_from(self.file_name_json)
        for note_item in self.database_in_memory:
            if note_item["note_id"] == note_id:
                self.print_one_note_beautyfully(note_item)

    def print_note_by_date(self, date_of_note: str):
        self.import_database_from(self.file_name_json)
        # print("Сработала заглушка для введенной даты " + str(date_of_note) )
        for note_item in self.database_in_memory:
            if note_item["changed_date"] == date_of_note:
                self.print_one_note_beautyfully(note_item)

    def print_one_note_beautyfully(self, note_item: dict):
        self.import_database_from(self.file_name_json)
        tab = str("    ")
        print(str("id: ") + str(note_item["note_id"]) + tab + str("Заголовок: ") + note_item["note_title"] + tab + str(
            "Содержание: ") + note_item["note_body"] + tab + str("Изменено: ") + note_item["changed_date"] + "  " +
              note_item["changed_time"])

    def test(self):
        return self.database_in_memory[-1]

    def get_one_note_from_position(self, value: int):
        self.import_database_from(self.file_name_json)
        return self.database_in_memory[value]

    # для выбора 4 ////////////////////////////////////////////////////////////
    def find_max_note_id(self) -> int:
        list_of_id = list()
        self.import_database_from(self.file_name_json)
        for note_item in self.database_in_memory:
            list_of_id.append(int(note_item["note_id"]))
        # print("Список id номеров: ", end="")
        # print(list_of_id)
        # print("А это максимум: " + str(max(list_of_id)))
        return max(list_of_id)

    def get_note_title_from_user(self) -> str:
        print("Введите заголовок будущей заметки >> ", end="")
        user_gave_us_a_note_title = str(input())
        return user_gave_us_a_note_title

    def get_note_body_from_user(self) -> str:
        print("Введите содержание будущей заметки >> ", end="")
        user_gave_us_a_note_body = str(input())
        return user_gave_us_a_note_body

    def create_new_note_content(self) -> dict:
        self.import_database_from(self.file_name_json)
        current_date = datetime.now().strftime("%Y-%m-%d")  # Получение текущей даты в формате "год-месяц-день"
        current_time = datetime.now().strftime("%H:%M")  # Получение текущего времени в формате "час:минута"

        new_note = {
            "note_id": int(self.find_max_note_id() + 1),  # Генерируйте уникальный note_id
            "note_title": str(self.get_note_title_from_user()),
            "note_body": str(self.get_note_body_from_user()),
            "changed_date": str(current_date),
            "changed_time": str(current_time)
        }
        database_in_memory = list(self.database_in_memory)
        database_in_memory.append(new_note)
        return database_in_memory

    def append_new_note(self, database_from_memory):
        # Запись обновленных данных в JSON-файл
        with open(self.file_name_json, "w", encoding="utf-8") as json_file:
            json.dump(database_from_memory, json_file, indent=2, ensure_ascii=False)

    def handler4(self):
        database_in_memory = self.create_new_note_content()
        self.append_new_note(database_in_memory)

    # ///////////////////////////////////////////////////////////////////////

    # начало для выбора 5 ////////////////////////////////////////////////////////////
    def handler5(self):
        self.import_database_from(self.file_name_json)
        database_in_memory = list(self.database_in_memory)

        print("Введите номер id для удаления заметки >> ", end="")
        user_gave_us_an_id_number = int(input())

        # Поиск заметки с заданным note_id и удаление её
        for note in database_in_memory:
            if int(str(note["note_id"]).replace(" ", "")) == int(user_gave_us_an_id_number):
                database_in_memory.remove(note)
                break  # Выход из цикла после удаления первой заметки с указанным note_id
        self.append_new_note(database_in_memory)

    # конец для выбора 5 ////////////////////////////////////////////////////////////

    # начало для выбора 6 ////////////////////////////////////////////////////////////
    def handler6(self):
        print("Введите номер id для изменения заметки >> ", end="")
        user_gave_us_an_id_number = int(input())
        self.delete_old_note_by(user_gave_us_an_id_number)
        self.edite_old_note_content(user_gave_us_an_id_number)


    def delete_old_note_by(self, id):
        self.import_database_from(self.file_name_json)
        database_in_memory = list(self.database_in_memory)

        user_gave_us_an_id_number = id
        # Поиск заметки с заданным note_id и удаление её
        for note in database_in_memory:
            if int(str(note["note_id"]).replace(" ", "")) == int(user_gave_us_an_id_number):
                database_in_memory.remove(note)
                break  # Выход из цикла после удаления первой заметки с указанным note_id
        self.append_new_note(database_in_memory)

    def edite_old_note_content(self, id):
        self.import_database_from(self.file_name_json)
        current_date = datetime.now().strftime("%Y-%m-%d")  # Получение текущей даты в формате "год-месяц-день"
        current_time = datetime.now().strftime("%H:%M")  # Получение текущего времени в формате "час:минута"

        new_note = {
            "note_id": int(id),  # Генерируйте уникальный note_id
            "note_title": str(self.get_note_title_from_user()),
            "note_body": str(self.get_note_body_from_user()),
            "changed_date": str(current_date),
            "changed_time": str(current_time)
        }
        database_in_memory = list(self.database_in_memory)
        database_in_memory.append(new_note)
        self.append_new_note(database_in_memory)

    # конец для выбора 6 ////////////////////////////////////////////////////////////
