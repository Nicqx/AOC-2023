from unittest import TestCase

from Days.Day1 import Day1


class TestDay1(TestCase):

    def test_task1(self):
        expected_value = str(142)
        actual_value = Day1('../Resources/Day1/test').task1()
        self.assertEqual(expected_value, actual_value)

    def test_task2(self):
        expected_value = str(281)
        actual_value = Day1('../Resources/Day1/test2').task2()
        self.assertEqual(expected_value, actual_value)

    def test_original(self):
        expected_value_task1 = str(54081)
        expected_value_task2 = str(54649)
        d1 = Day1('../Resources/Day1/input')
        actual_value_task1 = d1.task1()
        self.assertEqual(expected_value_task1, actual_value_task1)
        actual_value_task2 = d1.task2()
        self.assertEqual(expected_value_task2, actual_value_task2)
