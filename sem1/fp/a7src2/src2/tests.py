from src2.services import Services
from repository import MemoryRepository

class Tests:
    def __init__(self):
        repository = MemoryRepository()
        self.services = Services(repository)
        self.logs = []

    def print_logs(self):
        for log in self.logs:
            print(log)

    def test_all(self):
        self.test_number_str_to_dict()
        self.test_add_number()
        self.print_logs()

    def test_number_str_to_dict(self):
        self.logs.append("Test number str to dict")
        numbers_to_test = [
            "32  -  23 8  i",
            "asdsfs",
            "-1+1i",
            "12a43i",
            "23-34j"
        ]

        for number in numbers_to_test:
            try:
                self.services.number_str_to_dict(number)
            except ValueError as ve:
                self.logs.append(ve)
            else:
                self.logs.append("Valid number")

        self.logs.append("---------------")

    def test_add_number(self):
        self.logs.append("Test add number")

        try:
            self.services.add_number("23-34i")
            self.services.add_number("sdfsdf")
        except ValueError:
            assert True

        try:
            assert str(self.services.get_number_list()[-1]) == "23-34i"
        except AssertionError as ae:
            self.logs.append(ae)
        else:
            self.logs.append("Valid addition")