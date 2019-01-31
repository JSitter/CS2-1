#!python

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
      list_a = items[0:middle]
      list_b = items[middle + 1: len(list_a) - 1]
    else:
      return items
    
    # Sort list A
    insertion_sort(list_a)

    # Sort list B
    insertion_sort(list_b)

    # Merge sorted halves into one list in sorted order
    return merge(list_a, list_b)




def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order

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


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
  """Sort given items in place by partitioning items in range `[low...high]`
  around a pivot item and recursively sorting each remaining sublist range.
  TODO: Best case running time: ??? Why and under what conditions?
  TODO: Worst case running time: ??? Why and under what conditions?
  TODO: Memory usage: ??? Why and under what conditions?"""
  # TODO: Check if high and low range bounds have default values (not given)
  # TODO: Check if list or range is so small it's already sorted (base case)
  # TODO: Partition items in-place around a pivot and get index of pivot
  # TODO: Sort each sublist range by recursively calling quick sort
  pass

if __name__ == "__main__":
  print(merge([3,4,7], [1, 3, 5, 8]))