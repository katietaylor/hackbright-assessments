#Sorting

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """

    for i in range(len(lst) - 1):
        has_swapped = False
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                has_swapped = True
        # check if a swap was made to see if already sorted.
        if not has_swapped:
            break

    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    merged_list = []

    index_1 = 0
    index_2 = 0

    while len(merged_list) < (len(list1) + len(list2)):

        # all values in list1 complete, append next value in list2
        if index_1 == len(list1):
            merged_list.append(list2[index_2])
            index_2 += 1

        # all values in list2 complete, append next value in list1
        elif index_2 == len(list2):
            merged_list.append(list1[index_1])
            index_1 += 1

        # append smallest value, which is the next value in list1
        elif list1[index_1] < list2[index_2]:
            merged_list.append(list1[index_1])
            index_1 += 1

        # append smallest value, which is next value in list2
        elif list2[index_2] < list1[index_1]:
            merged_list.append(list2[index_2])
            index_2 += 1

        # values equal, append both
        elif list2[index_2] == list1[index_1]:
            merged_list.append(list1[index_1])
            index_1 += 1
            merged_list.append(list2[index_2])
            index_2 += 1

    return merged_list


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """

    if len(lst) < 2:
        return lst

    midpoint = len(lst) / 2

    list1 = merge_sort(lst[:midpoint])
    list2 = merge_sort(lst[midpoint:])

    return merge_lists(list1, list2)


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
