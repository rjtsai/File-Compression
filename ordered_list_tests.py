import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):
    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)


    def test_ordered_progression(self):
        ordList = OrderedList()
        self.assertTrue(ordList.is_empty())

        ordList.add(10)
        self.assertFalse(ordList.is_empty())
        self.assertFalse(ordList.add(10))   #  tests duplicate entry
        self.assertEqual(ordList.python_list(), [10])  # tests list

        ordList.add(20)
        self.assertEqual(ordList.size(), 2)  # tests size
        self.assertEqual(ordList.python_list(), [10, 20])  # tests list

        ordList.add(15)
        self.assertEqual(ordList.python_list(), [10, 15, 20]) # tests adding to middle
        self.assertEqual(ordList.python_list_reversed(), [20, 15, 10]) # tests reverse list

        self.assertEqual(ordList.index(15), 1)  # tests index()
        self.assertIsNone(ordList.index(50))

        self.assertTrue(ordList.remove(15))  # tests remove
        self.assertFalse(ordList.remove(50))
        self.assertEqual(ordList.python_list(), [10, 20])

        self.assertEqual(ordList.pop(1), 20)  # tests pop
        with self.assertRaises(IndexError):
            ordList.pop(5)

if __name__ == '__main__': 
    unittest.main()
