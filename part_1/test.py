import unittest
from solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.find_max = Solution().find_max

    def test_general_case(self):
        arr = [-6, 5, 3, 1, 0, -1, -10]
        self.assertEqual(self.find_max(arr), 5)

    def test_array_is_tiny(self):
        arr = [10]
        self.assertEqual(self.find_max(arr), 10)

        arr = [1, 2]
        self.assertEqual(self.find_max(arr), 2)

        arr = [-1, -2]
        self.assertEqual(self.find_max(arr), -1)

    def test_array_is_only_increasing(self):
        arr = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.find_max(arr), 6)

    def test_array_is_only_decreasing(self):
        arr = [5, 4, 0, -1, -2]
        self.assertEqual(self.find_max(arr), 5)


    def test_array_is_empty(self):
        arr = []
        self.assertEqual(self.find_max(arr), None)



if __name__ == '__main__':
    unittest.main()
