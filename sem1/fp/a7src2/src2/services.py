class Services:
    def __init__(self, repository):
        self.repository = repository

    def get_number_list(self):
        """
        The function returns the list of numbers.
        :return: the list of numbers
        """
        return self.repository.get_number_list()

    def number_str_to_dict(self, number):
        """
        The function returns a valid number from a string if it can
        :param number: the str number given
        :return: a dict number if it can
        """
        number = number.replace(" ", "")

        if len(number) < 4:
            raise ValueError("Invalid number")

        i = 0
        if number[0] == "-":
            i += 1
        while number[i].isdigit():
            i += 1

        if i == 0:
            raise ValueError("Invalid number")

        real_part = int(number[:i])

        if (number[i] != "+" and number[i] != "-") or number[-1] != "i":
            raise ValueError("Invalid number, the number doesent contain the right simbols")

        try:
            imaginary_part = int(number[i:-1])
        except ValueError:
            raise ValueError("Invalid number")

        return {"real": real_part, "imaginary": imaginary_part}

    def add_number(self, number):
        """
        The function adds a number to the repository list.
        :param number: the number to be added to the repository list as a string
        :return: nothing
        """
        good_number = self.number_str_to_dict(number)
        self.repository.add_number(good_number)

    def validate_indexes(self, starting_index, ending_index):
        """
        The function checks if the indexes can be integers and if the starting index is greater than the ending index.
        :param starting_index: the starting index as a string
        :param ending_index: the ending index as a string
        :return: the indexes as ints if they respect the conditions
        """
        try:
            int_si = int(starting_index)
            int_ei = int(ending_index)
        except ValueError:
            raise ValueError("Indexes must be integers")

        if int_si > int_ei:
            raise ValueError("The starting index cannot be greater than the ending index")

        return int_si, int_ei

    def filter_list(self, starting_index, ending_index):
        """
        The functions filter the repository list by deleting the numbers that are not between the given indexes.
        :param starting_index: the starting index as a string
        :param ending_index: the ending index as a string
        :return: nothing
        """

        number_list = self.repository.get_number_list()
        int_start, int_end = self.validate_indexes(starting_index, ending_index)

        if not (int_start < len(number_list) and int_end < len(number_list)):
            raise ValueError("Indexes are out of range")

        number_list = number_list[int_start:int_end + 1]

        self.repository.update_number_list(number_list)

    def undo(self):
        """
        Undo the last operation modifying command
        :return: nothing
        """
        self.repository.undo()

    def update_repo(self, new_repo):
        self.repository = new_repo