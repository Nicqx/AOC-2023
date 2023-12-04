import re

from Utilities.read_file_to_string_array import read_to_array


class Day3:
    arr = []
<<<<<<< HEAD
    points = []
=======
    mat = []
>>>>>>> origin/main

    def __init__(self, file):
        self.arr.clear()
        self.arr = read_to_array(file)
<<<<<<< HEAD

    def task1(self):
        result = 0
        self.convert_array_to_points()

        self.validate_numbers()

        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                self.activate_number(j, i)

        validated_numbers = self.get_string_from_valid_numbers()

        mo = re.findall(r'\d+', validated_numbers)
        for item in mo:
            result += int(item)
=======
        self.mat = self.convert_array_to_matrix(self.arr)

    def task1(self):
        result = 0
>>>>>>> origin/main

        return str(result)

    def task2(self):
        result = 0

        return str(result)

<<<<<<< HEAD
    def activate_number(self, x, y):
        if self.get_point(x, y).get_keep() and self.get_point(x, y).get_type() == "number":
            if x > 0:
                if self.get_point(x - 1, y).get_type() == "number" and not (self.get_point(x - 1, y).get_keep()):
                    self.get_point(x - 1, y).set_keep()
                    self.activate_number(x - 1, y)
            if x < len(self.arr[0]) - 1:
                if self.get_point(x + 1, y).get_type() == "number" and not (self.get_point(x + 1, y).get_keep()):
                    self.get_point(x + 1, y).set_keep()
                    self.activate_number(x + 1, y)
            if y > 0:
                if self.get_point(x, y - 1).get_type() == "number" and not (self.get_point(x, y - 1).get_keep()):
                    self.get_point(x, y - 1).set_keep()
                    self.activate_number(x, y - 1)
            if y < len(self.arr) - 1:
                if self.get_point(x, y + 1).get_type() == "number" and not (self.get_point(x, y + 1).get_keep()):
                    self.get_point(x, y + 1).set_keep()
                    self.activate_number(x, y + 1)
            if x > 0 and y > 0:
                if self.get_point(x - 1, y - 1).get_type() == "number" and not (
                        self.get_point(x - 1, y - 1).get_keep()):
                    self.get_point(x - 1, y - 1).set_keep()
                    self.activate_number(x - 1, y - 1)
            if x < len(self.arr[0]) - 1 and y > 0:
                if self.get_point(x + 1, y - 1).get_type() == "number" and not (
                        self.get_point(x + 1, y - 1).get_keep()):
                    self.get_point(x + 1, y - 1).set_keep()
                    self.activate_number(x + 1, y - 1)
            if x > 0 and y < len(self.arr) - 1:
                if self.get_point(x - 1, y + 1).get_type() == "number" and not (
                        self.get_point(x - 1, y + 1).get_keep()):
                    self.get_point(x - 1, y + 1).set_keep()
                    self.activate_number(x - 1, y + 1)
            if x < len(self.arr[0]) - 1 and y < len(self.arr) - 1:
                if self.get_point(x + 1, y + 1).get_type() == "number" and not (
                        self.get_point(x + 1, y + 1).get_keep()):
                    self.get_point(x + 1, y + 1).set_keep()
                    self.activate_number(x + 1, y + 1)

    def validate_numbers(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                if self.check_neigh(j, i):
                    self.get_point(j, i).set_keep()

    def get_string_from_valid_numbers(self):
        result = ""
        x = 0
        for element in self.points:
            x += 1
            if element.get_type() == "number" and element.get_keep():
                result = result + element.get_value()
            else:
                result = result + "."
            if x % len(self.arr[0]) == 0:
                result = result + "."
        return result

    def convert_array_to_points(self):

        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                self.points.append(Point(j, i, self.arr[i][j]))

    def check_neigh(self, x, y):
        if x > 0:
            if self.get_point(x - 1, y).get_type() == "symbol":
                return True
        if x < len(self.arr[0]) - 1:
            if self.get_point(x + 1, y).get_type() == "symbol":
                return True
        if y > 0:
            if self.get_point(x, y - 1).get_type() == "symbol":
                return True
        if y < len(self.arr) - 1:
            if self.get_point(x, y + 1).get_type() == "symbol":
                return True
        if x > 0 and y > 0:
            if self.get_point(x - 1, y - 1).get_type() == "symbol":
                return True
        if x < len(self.arr[0]) - 1 and y > 0:
            if self.get_point(x + 1, y - 1).get_type() == "symbol":
                return True
        if x > 0 and y < len(self.arr) - 1:
            if self.get_point(x - 1, y + 1).get_type() == "symbol":
                return True
        if x < len(self.arr[0]) - 1 and y < len(self.arr) - 1:
            if self.get_point(x + 1, y + 1).get_type() == "symbol":
                return True

    def get_point(self, x, y):
        for item in self.points:
            if item.get_coord() == (x, y):
                return item


class Point:
    type = ""  # point, number, symbol
    keep = False
    coord = ()
    value = ""

    def __init__(self, x, y, t):
        self.coord = ()
        self.type = ""
        self.keep = False
        self.value = ""
        self.coord = (x, y)
        mo = re.match(r'\d', t)
        mo2 = re.match(r'\.', t)
        if mo:
            self.type = "number"
            self.value = t
        elif mo2:
            self.type = "point"
        else:
            self.type = "symbol"

    def get_type(self):
        return self.type

    def get_coord(self):
        return self.coord

    def get_value(self):
        return self.value

    def get_keep(self):
        return self.keep

    def set_keep(self):
        self.keep = True
=======
    @staticmethod
    def convert_array_to_matrix(arr):
        result = []
        for item in arr:
            result.append(list(item))
        return result

    class Point:
        type = "" # point, number, symbol
        checked = False
>>>>>>> origin/main
