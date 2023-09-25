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

    def print_one_note_beautyfully(self, note_item: dict):
        self.import_database_from(self.file_name_json)
        tab = str("    ")
        print(str("id: ") + str(note_item["note_id"]) + tab + str("Заголовок: ") + note_item["note_title"] + tab + str("Содержание: ") + note_item["note_body"] + tab + str("Изменено: ") + note_item["changed_date"] + "  " + note_item["changed_time"])

    def test(self):
        return self.database_in_memory[-1]

    def get_one_note_from_position(self, value: int):
        self.import_database_from(self.file_name_json)
        return self.database_in_memory[value]
