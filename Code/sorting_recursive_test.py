#!python

from sorting_recursive import merge
import unittest

class mergeTest(unittest.TestCase):
    
    def test_merge_sorted_lists(self):
      new_list = merge([3,6,7,14,17], [1, 3, 4, 7, 10])
      assert all( [ a_value == b_value for a_value, b_value in zip(new_list, [1, 3, 3, 4, 6, 7, 7, 10, 14, 17])])
    
    def test_merge_with_empty_list(self):
      new_list = merge([1, 2, 3, 4], [])
      assert all( [ a_value == b_value for a_value, b_value in zip(new_list, [1, 2, 3, 4])])

    def test_merge_with_single_value(self):
      new_list = merge([1], [])
      assert all( [ a_value == b_value for a_value, b_value in zip(new_list, [1])])