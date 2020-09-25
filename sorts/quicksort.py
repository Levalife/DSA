"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):

    if len(array) <= 1:
        return array

    pivot = len(array) - 1
    i = 0

    for j in range(i, pivot):
        if array[i] > array[pivot]:
            temp = array[pivot]
            array[pivot] = array[i]
            array[i] = array[pivot - 1]
            array[pivot - 1] = temp
            pivot -= 1
        else:
            i += 1
        print(array)
    return quicksort(array[:pivot]) + [array[pivot]] + quicksort(array[pivot + 1:])


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
# test = [21, 4, 1, 3, 9]
print(quicksort(test))