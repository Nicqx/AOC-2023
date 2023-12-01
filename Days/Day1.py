import re
from copy import copy

from Utilities.read_file_to_string_array import read_to_array


class Day1:
    arr = []

    def __init__(self, file):
        self.arr.clear()
        self.arr = read_to_array(file)

    def task1(self):
        result = 0
        for row in self.arr:
            cv = ""
            for letter in row:
                if letter.isnumeric():
                    cv = cv + letter
                    break
            for letter in reversed(row):
                if letter.isnumeric():
                    cv = cv + letter
                    break
            result += int(cv)
        return str(result)

    def task2(self):
        word_list = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
        result = 0

        for row in self.arr:
            cv = ""
            copy_of_arr = copy(row)
            cv = cv + self.check_forward(copy_of_arr, word_list)
            copy_of_arr = copy(row)
            cv = cv + self.check_backward(copy_of_arr, word_list)
            result += int(cv)
        return str(result)

    @staticmethod
    def check_forward(szoveg, wl):
        if szoveg[0].isnumeric():
            return szoveg[0]
        else:
            while szoveg != "":
                if szoveg[0].isnumeric():
                    return szoveg[0]
                for element in wl.keys():
                    mo = re.match("^" + element, szoveg)
                    if mo:
                        return str(wl[element])
                szoveg = szoveg[1:]

    @staticmethod
    def check_backward(szoveg, wl):
        if szoveg[-1].isnumeric():
            return szoveg[-1]
        else:
            while szoveg != "":
                if szoveg[-1].isnumeric():
                    return szoveg[-1]
                for element in wl.keys():
                    mo = re.match(".*" + element + "$", szoveg)
                    if mo:
                        return str(wl[element])
                szoveg = szoveg[:-1]
