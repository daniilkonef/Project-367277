from datamodel_pack.database_class import CreateDatabaseMachine


class CreatePresenterObject:
    database_machine = None

    def __init__(self, database_machine: CreateDatabaseMachine):
        self.database_machine = database_machine

    def show_3_last_notes(self):
        self.database_machine.print_note_by_id(1)
        self.database_machine.print_note_by_id(2)
        self.database_machine.print_note_by_id(3)

    def show_all_notes(self):
        self.database_machine.print_all_notes()

    def show_empty_lines(self, count: int):
        for i in range(count):
            print()
