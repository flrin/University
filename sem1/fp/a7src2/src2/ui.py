import texttable as tt
from src2.services import Services
from domain import Complex

class Ui:
    def __init__(self, services : Services):
        self.services = services
        self.command_functions_dict = {
            "1" : self.add_number_scenario,
            "2" : self.display_list,
            "3" : self.filter_list_scenario,
            "4" : self.undo_list_scenario,
            "5" : self.exit_scenario
        }

    def print_menu(self):
        print('''
            1. Add a number. The number is read from the console.
            2. Display the list of numbers.
            3. Filter the list so that it contains only the numbers between indices start and end, where these values are read from the console.
            4. Undo the last operation that modified program data. This step can be repeated. The user can undo only those operations made during the current run of the program.
            5. Exit the program.
        ''')

    def start_loop(self):
        while True:
            self.print_menu()
            command = input(">>")

            if command in self.command_functions_dict.keys():
                self.command_functions_dict[command]()
            else:
                print("Invalid command")

    def add_number_scenario(self):
        number = input("The number to be added: ")
        try:
            self.services.add_number(number)
        except ValueError as ve:
            print(ve)

    def display_list(self):
        table = tt.Texttable()
        table.add_row(["Index", "Real Part", "Imaginary Part"])
        table.set_cols_align(["c", "c", "c"])

        number_list = self.services.get_number_list()

        for i in range(len(number_list)):
            real = number_list[i].get_real_part()
            imaginary = number_list[i].get_imaginary_part()
            table.add_row([i, real, imaginary])

        print(table.draw())

    def filter_list_scenario(self):
        starting_index = input("The starting index: ")
        ending_index = input("The ending index: ")
        try:
            self.services.filter_list(starting_index, ending_index)
        except ValueError as ve:
            print(ve)

    def undo_list_scenario(self):
        self.services.undo()

    def exit_scenario(self):
        exit(0)