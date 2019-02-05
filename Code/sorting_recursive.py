#!python
import random

def merge(items1, items2):
  """Merge given lists of items, each assumed to already be in sorted order,
  and return a new list containing all items in sorted order.

  Running time: Always O(NM) where N is the length of the first list and M is the length of the second list. 
  Memory usage: O(NM) Because a new list is created at the same length of both lists combined."""
  # Repeat until one list is empty
  # Find minimum item in both lists and append it to new list
  # Append remaining items in non-empty list to new list

  list_1_inx = 0
  list_2_inx = 0
  new_list = []
  # Add lowest value to new list
  if len(items1) == 0:
    return items2
  elif len(items2) == 0:
    return items1
  while len(items1) > list_1_inx and len(items2) > list_2_inx:
    if items1[list_1_inx] <= items2[list_2_inx]:
      # print("{} is less than or equals {}. Append {}".format(items1[list_1_inx], items2[list_2_inx], items1[list_1_inx]))
      new_list.append(items1[list_1_inx])

      list_1_inx += 1
    else:
      # print("{} is less than {}. Append {}".format(items2[list_2_inx], items1[list_1_inx], items2[list_2_inx]))
      new_list.append(items2[list_2_inx])
      list_2_inx += 1
    # print("List One index: {}\nList 2 Index: {}".format(list_1_inx, list_2_inx))
    # print("Current New list: {}".format(new_list))

  # List 2 has completed 
  # Add the rest of the List 1
  while list_1_inx <= (len(items1) - 1):
    new_list.append(items1[list_1_inx])
    list_1_inx += 1

  # List 2 has completed 
  # Add the rest of the List 1    
  while list_2_inx <= (len(items2) - 1):
    new_list.append(items2[list_2_inx])
    list_2_inx += 1

  print(new_list)

  return new_list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    if len(items) > 2:
      middle = len(items) // 2
      list_a = items[:middle]
      list_b = items[middle :]
    else:
      return items
    
    # Sort list A
    sorted_a = insertion_sort(list_a)

    # Sort list B
    sorted_b = insertion_sort(list_b)
    print("List a: {}, List b: {}".format(sorted_a, sorted_b))
    # Merge sorted halves into one list in sorted order
    return merge(sorted_a, sorted_b)




def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Check if list is so small it's already sorted (base case)
    if ( len(items) <=1 ):
      return items

    # Split items list into approximately equal halves
    mid = len(items)//2
    list_a = items[:mid]
    list_b = items[mid:]

    # Sort each half by recursively calling merge sort
    sorted_a = merge_sort(list_a)
    sorted_b = merge_sort(list_b)

    # Merge sorted halves into one list in sorted order
    sorted_lists =  merge(sorted_a, sorted_b)
    print(sorted_lists)
    return sorted_lists


# This code was pulled from My CS2 Sorting Repository
def insertion_sort(items):
    """Sort given items by taking first unsorted items, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n^2) 
    Memory usage: O(n)"""

    # Repeat until all items are in sorted order
    for unsort_index in range(1, len(items)):
        sort_item = items[unsort_index]
        compare_index = unsort_index - 1
        item_sorted = False
        insert_index = unsort_index
        while not item_sorted:
            if items[compare_index] < sort_item:
                items[insert_index] = sort_item
                item_sorted = True
            else:
                #move compared item down and check
                items[insert_index] = items[compare_index]
                if compare_index == 0:
                    items[compare_index] = sort_item
                    item_sorted = True
                else:
                    insert_index -= 1
                    compare_index -= 1
    print(items)
    return items


def partition(items, low, high):
  
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot randomly from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Choose a random pivot, on average will be median value due to central limit theorem.
    pivot_index = random.randint(low, high)
    high_val = items[high]
    items[high] = items[pivot_index]
    items[pivot_index] = high_val
    pivot_index = high
    high -= 1
    

    # Loop through all items in range [low...high] from ends
    while low < high:
      while items[low] < items[pivot_index]:
        low += 1
      while items[high] > items[pivot_index]:
        high -= 1
      
      # Swap
      if items[low] > items[high]:
        temp = items[low]
        items[low] = items[high]
        items[high] = temp
    
    #Replace Pivot
    high_item = items[low]

    items[low] = items[pivot_index]
    items[pivot_index] = high_item

    # Move pivot item into final position [p] and return index p
    return low

def quick_sort(items, low=None, high=None):
  """Sort given items in place by partitioning items in range `[low...high]`
  around a pivot item and recursively sorting each remaining sublist range.
  TODO: Best case running time: ??? Why and under what conditions?
  TODO: Worst case running time: ??? Why and under what conditions?
  TODO: Memory usage: ??? Why and under what conditions?"""
  # TODO: Check if high and low range bounds have default values (not given)
  if low is None:
    low = 0
  
  if high is None:
    high = len(items) - 1

  # Check if list or range is so small it's already sorted (base case)
  if len(items) < 2:
    return items

  # TODO: Partition items in-place around a pivot and get index of pivot
  low_index = partition(items, low, high)
  # TODO: Sort each sublist range by recursively calling quick sort
  quick_sort(items, 0, low_index)
  quick_sort(items, low_index, high)