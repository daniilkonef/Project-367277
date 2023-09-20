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
        tab = str("    ")
        print(str("id: ") + str(note_item["note_id"]) + tab + str("title: ") + note_item["note_title"] + tab + str(
            "changed: ") + note_item["changed_date"] + "  " + note_item["changed_time"])
