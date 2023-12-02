import re
from copy import copy

from Utilities.read_file_to_string_array import read_to_array


class Day2:
    arr = []
    games = {}

    def __init__(self, file):
        self.arr.clear()
        self.arr = read_to_array(file)
        self.games = self.parse_data(self.arr)

    def task1(self):
        result = 0
        for game in self.games.keys():
            if self.check_for_colors(self.games[game]):
                result += game
        return str(result)

    def task2(self):
        result = 0

        for game in self.games.keys():
            one_game = self.get_game_max(self.games[game])
            result += one_game['red'] * one_game['green'] * one_game["blue"]

        return str(result)

    @staticmethod
    def get_game_max(line):
        result = {'red': 0, 'green': 0, 'blue': 0}
        blocks = line.split(';')
        for block in blocks:
            mo = re.search(r'(\d+) red', block)
            if mo and result["red"] < int(mo.group(1)):
                result["red"] = int(mo.group(1))
            mo = re.search(r'(\d+) green', block)
            if mo and result["green"] < int(mo.group(1)):
                result["green"] = int(mo.group(1))
            mo = re.search(r'(\d+) blue', block)
            if mo and result["blue"] < int(mo.group(1)):
                result["blue"] = int(mo.group(1))

        return result

    @staticmethod
    def check_for_colors(line):
        result = True
        blocks = line.split(';')
        for block in blocks:
            block_result = True
            mo = re.search(r'(\d+) red', block)
            if mo and int(mo.group(1)) > 12:
                block_result = False
            mo = re.search(r'(\d+) green', block)
            if mo and int(mo.group(1)) > 13 and block_result:
                block_result = False
            mo = re.search(r'(\d+) blue', block)
            if mo and int(mo.group(1)) > 14 and block_result:
                block_result = False
            result = result and block_result
        return result

    @staticmethod
    def parse_data(arr):
        games = {}
        for line in arr:
            mo = re.match(r'Game (\d+): (.*)', line)
            if mo:
                games[int(mo.group(1))] = mo.group(2)
        return games
