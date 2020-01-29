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
    output_index = linear_search_recursive(array, item, index + 1)
    return output_index


def binary_search(array, item):
    """Return the index of item in sorted array or None if item is not found."""

    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative_1(array, item):
    # 1, 2, 2, 3, 4, 6, 8, 9
    # 0  1  2  3  4  5  6  7
    pass





def binary_search_iterative(array, item):

    # 1, 2, 2, 3, 4, 6, 8, 9
    # 0  1  2  3  4  5  6  7

    indexx = 10
    middle_index = int(len(array) / 2)
    original_index = middle_index

    print("=============")
    print("Loooking for {}".format(item))
    print("=============")

    while indexx != 0:

        print("Middle index: {} -> array[{}]: {}".format(middle_index, middle_index, array[middle_index]))

        if item == array[middle_index]:
            return original_index

        if item > array[middle_index]:
            print("{} is MORE than array[{}]: {}".format(item, middle_index, array[middle_index]))
            array = array[(middle_index + 1):]
            print("New array: {}".format(array))
            middle_index = int(len(array) / 2)
            original_index += (middle_index)
            print("New Original index: {}".format(original_index))
            print("New middle index: {}".format(middle_index))
        else:
            print("{} is LESS than array[{}]: {}".format(item, middle_index, array[middle_index]))
            array = array[:(middle_index)]
            print("New array: {}".format(array))
            middle_index = int(len(array) / 2)
            original_index -= (middle_index + 1)
            print("New Original index: {}".format(original_index))
            print("New middle index: {}".format(middle_index))

        indexx -= 1




    # print("=====================")
    # print("Looking for {}".format(item))
    # print("=====================")
    #
    # start_index = 0
    # end_index = len(array)
    # middle_index = int(len(array) / 2)
    #
    # array_size = end_index - start_index
    #
    # indexx = 10
    #
    # while(indexx != 0):
    #
    #     print("Middle index: {} -> array[{}]: {}".format(middle_index, middle_index, array[middle_index]))
    #
    #     if item == array[middle_index]:
    #         print("Found item")
    #         return middle_index
    #
    #     if item > array[middle_index]:
    #         print("{} is MORE than array[{}]: {}".format(item, middle_index, array[middle_index]))
    #         start_index = middle_index + 1
    #         middle_index = int((end_index - start_index) / 2)
    #         print("New: start-index: {} middle-index: {}  end-index: {}".format(start_index, middle_index, end_index))
    #     else:
    #         print("{} is LESS than array[{}]: {}".format(item, middle_index, array[middle_index]))
    #         end_index = middle_index - 1
    #         middle_index = int((end_index - start_index) / 2)
    #         # middle_index = middle_index - int((end_index - start_index) / 2)
    #         print("New: start-index: {} middle-index: {}  end-index: {}".format(start_index, middle_index, end_index))
    #
    #     array_size = end_index - start_index
    #     indexx = indexx - 1
    #
    # return None

def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
