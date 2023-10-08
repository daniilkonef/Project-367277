import json


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
        print("Список id номеров: ", end="")
        print(list_of_id)
        print("А это максимум: " + str(max(list_of_id)))
        return max(list_of_id)

    def create_note_content(self):
        self.import_database_from(self.file_name_json)
        # Ваша новая заметка (замените этот словарь своими данными)
        new_note = {
            "note_id": self.find_max_note_id() + 1,  # Генерируйте уникальный note_id
            "note_title": "Новая заметка от ЧатДжиПиТи",
            "note_body": "Текст вашей заметки от ЧатДжиПиТи",
            "changed_date": "2023-09-24 от ЧатДжиПиТи",
            "changed_time": "14:30 от ЧатДжиПиТи"
        }
        database_in_memory = list(self.database_in_memory)
        database_in_memory.append(new_note)
        print(database_in_memory)

        # Запись обновленных данных в JSON-файл
        with open(self.file_name_json, "w", encoding="utf-8") as json_file:
            json.dump(database_in_memory, json_file, indent=2, ensure_ascii=False)




    # ///////////////////////////////////////////////////////////////////////