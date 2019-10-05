import unittest

# mine
import sorting_algorithms

class TestSortingAlgorithms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.unsorted_list = [333, 0, -7, -12, 201, 3]
        cls.sorted_list = [-12, -7, 0, 3, 201, 333]

    def test_selection_sort(self):
        actual_sorted = sorting_algorithms.selection_sort(
            TestSortingAlgorithms.unsorted_list)
        self.assertEqual(actual_sorted, TestSortingAlgorithms.sorted_list)