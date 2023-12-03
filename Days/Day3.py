import re

from Utilities.read_file_to_string_array import read_to_array


class Day3:
    arr = []
    mat = []

    def __init__(self, file):
        self.arr.clear()
        self.arr = read_to_array(file)
        self.mat = self.convert_array_to_matrix(self.arr)

    def task1(self):
        result = 0

        return str(result)

    def task2(self):
        result = 0

        return str(result)

    @staticmethod
    def convert_array_to_matrix(arr):
        result = []
        for item in arr:
            result.append(list(item))
        return result

    class Point:
        type = "" # point, number, symbol
        checked = False