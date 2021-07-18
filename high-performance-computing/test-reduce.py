import unittest

import reduce

class TestReduce(unittest.TestCase):
    def test_thing(self):
        self.assertTrue(True)
    
    def test_sequential_sum(self):
        expected = 20
        actual = reduce.sum_array([1,0,16,-3,6])
        self.assertEqual(expected, actual)

    def test_parallel_sum(self):
        expected = 20
        reduce.sum_array_static_parallel([1,0,16,-3,6])
        actual = reduce.SUM
        self.assertEqual(expected, actual)
