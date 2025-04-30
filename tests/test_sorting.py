import unittest
from sorting_algorithms import *

class TestSorting(unittest.TestCase):
    l1 = [5,1,7,-3]
    linked_list1 = convert_to_linked_list(l1)

    def test_bubble_sort_list(self):
        self.assertEqual(bubble_sort(self.l1), [-3, 1, 5, 7])

if __name__ == "__main__":
    unittest.main()

    