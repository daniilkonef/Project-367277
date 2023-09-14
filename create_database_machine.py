import json


class create_database_machine:
    database_in_memory = list()
    file_name_json = str("app_data_base.json")

    def import_database_from(self, file_name_json: str):
        with open(file_name_json, "r", encoding="utf-8") as my_json_file:
            self.database_in_memory = json.load(my_json_file)


    def print_all_notes(self):
        self.import_database_from(self.file_name_json)
        for item in self.database_in_memory:
            print(item)

