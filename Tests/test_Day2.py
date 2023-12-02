from unittest import TestCase

from Days.Day2 import Day2


class TestDay1(TestCase):

    def test_task1(self):
        expected_value = str(8)
        actual_value = Day2('../Resources/Day2/test').task1()
        self.assertEqual(expected_value, actual_value)

    def test_task2(self):
        expected_value = str(2286)
        actual_value = Day2('../Resources/Day2/test').task2()
        self.assertEqual(expected_value, actual_value)

    def test_original(self):
        expected_value_task1 = str(2268)
        expected_value_task2 = str(63542)
        d1 = Day2('../Resources/Day2/input')
        actual_value_task1 = d1.task1()
        self.assertEqual(expected_value_task1, actual_value_task1)
        actual_value_task2 = d1.task2()
        self.assertEqual(expected_value_task2, actual_value_task2)
