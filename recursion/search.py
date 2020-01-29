#!python3

def linear_search(array, item):
    """Return the first index of item in array or None if item is not found."""

    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
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

    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
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
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
