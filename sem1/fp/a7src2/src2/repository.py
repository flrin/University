import pickle as pk
from random import randint
import os
import json as js

from domain import Complex

class MemoryRepository:
    """
    A repository class used to store a list of complex numbers in memory
    It also generates 10 random numbers at startup
    """
    def __init__(self):
        self.number_list = self.generate_starting_numbers()
        self.number_list_history = []

    def generate_starting_numbers(self):
        numbers = []
        for i in range(10):
            real = randint(-10, 10)
            imag = randint(-10, 10)
            new_number = Complex(real, imag)
            numbers.append(new_number)
        return numbers

    def add_number(self, number):
        """
        The functions takes a dictionary number and transforms it into a Complex object, and after that it appends it to the list.
        :param number: the number to be added as a dictionary
        """
        self.number_list_history.append(self.number_list.copy())
        new_number = Complex(number["real"], number["imaginary"])
        self.number_list.append(new_number)

    def get_number_list(self):
        return self.number_list

    def update_number_list(self, new_number_list):
        self.number_list_history.append(self.number_list.copy())
        self.number_list.clear()
        self.number_list = new_number_list

    def undo(self):
        if len(self.number_list_history) > 0:
            self.number_list = self.number_list_history[-1]
            self.number_list_history.pop()

class TextFileRepository:
    """
    A repository class used to store a list of complex numbers in a basic textfile.
    The contents of the file are deleted and updated with every change on the numbers.
    It also generates 10 random numbers at startup
    """

    def __init__(self):
        number_list = self.get_number_list()
        if len(number_list) == 0:
            self.store_numbers(self.generate_starting_numbers())
        self.number_list_history = []

    def get_number_list(self):
        number_list = []
        with open('numbers.txt', 'r') as file:
            raw_list = file.read().splitlines()

        for num in raw_list:
            split_number = num.split()
            new_number = Complex(int(split_number[0]), int(split_number[1]))
            number_list.append(new_number)

        return number_list

    def generate_starting_numbers(self):
        numbers = []
        for i in range(10):
            real = randint(-10, 10)
            imag = randint(-10, 10)
            new_number = Complex(real, imag)
            numbers.append(new_number)
        return numbers

    def store_numbers(self, number_list):
        with open ('numbers.txt', 'w') as file:
            for num in number_list:
                file.write(str(num) + "\n")

    def add_number(self, number):
        """
        The function takes a dictionary number and transforms it into a Complex object, and after that it adds it to the file.
        :param number: the number to be added as a dictionary
        """
        number_list = self.get_number_list()
        self.number_list_history.append(number_list.copy())
        new_number = Complex(number["real"], number["imaginary"])
        number_list.append(new_number)
        self.store_numbers(number_list)

    def update_number_list(self, new_number_list):
        self.number_list_history.append(self.get_number_list())
        self.store_numbers(new_number_list)

    def undo(self):
        if len(self.number_list_history) > 0:
            self.store_numbers(self.number_list_history[-1])
            self.number_list_history.pop()

class BinaryFileRepository:
    """
    A repository class used to store a list of complex numbers in a binary file, using the pickle module.
    The contents of the file are deleted and updated with every change on the numbers.
    It also generates 10 random numbers at startup
    """
    def __init__(self):
        if os.path.getsize('numbers.pickle') == 0:
            self.store_numbers(self.generate_starting_numbers())
        self.number_list_history = []

    def get_number_list(self):
        with open('numbers.pickle', 'rb') as file:
            number_list = pk.load(file)

        return number_list

    def generate_starting_numbers(self):
        numbers = []
        for i in range(10):
            real = randint(-10, 10)
            imag = randint(-10, 10)
            new_number = Complex(real, imag)
            numbers.append(new_number)
        return numbers

    def store_numbers(self, number_list):
        with open ('numbers.pickle', 'wb') as file:
            pk.dump(number_list, file)

    def add_number(self, number):
        """
        The function takes a dictionary number and transforms it into a Complex object, and after that it adds it to the file.
        :param number: the number to be added as a dictionary
        """
        number_list = self.get_number_list()
        self.number_list_history.append(number_list.copy())
        new_number = Complex(number["real"], number["imaginary"])
        number_list.append(new_number)
        self.store_numbers(number_list)

    def update_number_list(self, new_number_list):
        self.number_list_history.append(self.get_number_list())
        self.store_numbers(new_number_list)

    def undo(self):
        if len(self.number_list_history) > 0:
            self.store_numbers(self.number_list_history[-1])
            self.number_list_history.pop()

class JsonFileRepository:
    """
    A repository class used to store a list of complex numbers in a binary file, using the json module.
    The contents of the file are deleted and updated with every change on the numbers.
    It also generates 10 random numbers at startup
    """
    def __init__(self):
        if os.path.getsize('numbers.json') == 0:
            self.store_numbers(self.generate_starting_numbers())
        self.number_list_history = []

    def get_number_list(self):
        with open('numbers.json', 'r') as file:
            number_list = js.load(file)

        return [Complex(number["real"], number["imaginary"]) for number in number_list]

    def generate_starting_numbers(self):
        numbers = []
        for i in range(10):
            real = randint(-10, 10)
            imag = randint(-10, 10)
            new_number = Complex(real, imag)
            numbers.append(new_number)
        return numbers

    def store_numbers(self, number_list):
        with open ('numbers.json', 'w') as file:
            js.dump([number.to_dict() for number in number_list], file)

    def add_number(self, number):
        """
        The function takes a dictionary number and transforms it into a Complex object, and after that it adds it to the file.
        :param number: the number to be added as a dictionary
        """
        number_list = self.get_number_list()
        self.number_list_history.append(number_list.copy())
        new_number = Complex(number["real"], number["imaginary"])
        number_list.append(new_number)
        self.store_numbers(number_list)

    def update_number_list(self, new_number_list):
        self.number_list_history.append(self.get_number_list())
        self.store_numbers(new_number_list)

    def undo(self):
        if len(self.number_list_history) > 0:
            self.store_numbers(self.number_list_history[-1])
            self.number_list_history.pop()