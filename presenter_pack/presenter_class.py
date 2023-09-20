from datamodel_pack.database_class import CreateDatabaseMachine


class CreatePresenterObject:
    def __init__(self, database_machine: CreateDatabaseMachine):
        self.database_machine = database_machine

    def Show5LastNotes(self):
        self.database_machine.print_note_by_id(1)
        self.database_machine.print_note_by_id(2)
        self.database_machine.print_note_by_id(3)
