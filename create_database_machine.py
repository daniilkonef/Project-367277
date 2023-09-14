import json


class create_database_machine:
    database_in_memory = list()

    def import_database_from(self, file_name_json: str) -> list:
        with open("app_data_base.json", "r", encoding="utf-8") as my_json_file:
            self.database_in_memory = json.load(my_json_file)
            return self.database_in_memory

    def print_all_notes(self):
        self.import_database_from("app_data_base.json")
        for item in self.database_in_memory:
            print(item)
