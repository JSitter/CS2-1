#!python

from sorting_recursive import merge, split_sort_merge, merge_sort
import unittest

class mergeTest(unittest.TestCase):
    
    def test_merge_sorted_lists(self):
      new_list = merge([3,6,7,14,17], [1, 3, 4, 7, 10])
      assert all( [ a_value == b_value for a_value, b_value in zip(new_list, [1, 3, 3, 4, 6, 7, 7, 10, 14, 17])])
    
    def test_merge_with_empty_list(self):
      new_list = merge([1, 2, 3, 4], [])
      # Use list comprehension to check for matching values
      assert all( [ a_value == b_value for a_value, b_value in zip(new_list, [1, 2, 3, 4])])

    def test_merge_with_single_value(self):
      new_list = merge([1], [])
      assert all( [ a_value == b_value for a_value, b_value in zip(new_list, [1])])

    def test_split_sort_merge(self):
      new_list = split_sort_merge([3, 44, 23, 12, 34, 5, 6, 43, 34, 33])
      print(new_list)
      assert all( [a_value == b_value for a_value, b_value in zip(new_list, [3,5, 6, 12, 23, 33, 34, 34, 43, 44])])
    
