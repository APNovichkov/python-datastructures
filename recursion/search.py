#!python3

def linear_search(array, item):
    """Return the first index of item in array or None if item is not found."""

    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index
    return None


def linear_search_recursive(array, item, index=0):
    # Check if all of array has been traversed
    if index >= len(array):
        return None

    # Check if there is a match
    if item == array[index]:
        return index

    # Store output in output_index
    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """Return the index of item in sorted array or None if item is not found."""

    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # 1 2 4 5 6 7 9 9
    # 0 1 2 3 4 5 6 7

    start = 0
    end = len(array) - 1
    while(start <= end):
        middle = start + ((end - start) // 2)
        if item == array[middle]:
            return middle
        if item > array[middle]:
            start = middle + 1
        else:
            end = middle - 1

    return None

def binary_search_recursive(array, item, left=None, right=None):
    if left is None and right is None:
        left = 0
        right = len(array) - 1

    if(left > right):
        return None
    else:
        middle = left + (right - left) // 2
        if item == array[middle]:
            return middle
        if item > array[middle]:
            return binary_search_recursive(array, item, middle + 1, right)
        else:
            return binary_search_recursive(array, item, left, middle - 1)
