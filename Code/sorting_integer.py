#!python
import sys


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: O(n) Because the list of numbers is only iterated over a constant number of times.
    TODO: Memory usage: O(n) Because the original list is copied in the process."""
    # Find range of given numbers (minimum and maximum integer values)
    min = sys.maxsize
    max = 0
    for item in numbers:
      if item > max:
        max = item
      if item < min:
        min = item

    # Create list of counts with a slot for each number in input range
    number_list = [ 0 for i in range(max-min + 1)]
    # Array bucket is integer-min

    # Loop over given numbers and increment each number's count
    # print("Length of List: {}".format(len(number_list)))
    for integer in numbers:

      # print("Item: {}, index: {}".format(integer, (integer - min)))
      # print(integer - min)
      number_list[(integer - min)] += 1

    numbers = []
    # Loop over counts and append that many numbers into output list
    for key, value in enumerate(number_list):
      if value > 0:
        for _ in range(value):
          numbers.append(key + min)
    return numbers
      


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Find range of given numbers (minimum and maximum values)
    min = sys.maxsize
    max = 0
    for item in numbers:
      if item > max:
        max = item
      if item < min:
        min = item

    # Create list of buckets to store numbers in subranges of input range
    bucket_range = max - min

    bucket_list = [ [] for _ in range(num_buckets)]

    # Loop over given numbers and place each item in appropriate bucket
    for value in numbers:
      bucket_list[value%num_buckets].append(value)
    # Sort each bucket using any sorting algorithm (recursive or another)
    for num_list in bucket_list:
      num_list.sort()
    # Loop over buckets and append each bucket's numbers into output list
    new_list = []
    for num_list in bucket_list:
      for number in num_list:
        new_list.append(number)
    return new_list
    # FIXME: Improve this to mutate input instead of creating new output list

mylist = [34, 56, 45, 23, 57, 112, 2, 44, 56, 44, 67, 86, 94, 25, 53]
new_list = counting_sort(mylist)
print(new_list)

mylist = [34, 56, 45, 23, 57, 112, 2, 44, 56, 44, 67, 86, 94, 25, 53]
new_list = bucket_sort(mylist)
print(new_list)