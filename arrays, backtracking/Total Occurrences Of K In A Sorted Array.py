'''

a = [1, 1, 1, 2, 3]
k = 1
Result: 3

Best approach is to look for first occurance and last occurance of the element with the help of binary search
(two binary searches)

But it also possible to use binary search (for finding fragment with number) * linear search (counting all occurances)

'''


def total_occurances(a, k):
    first = binary_search(a, k, 0, len(a) - 1, "first")
    if first == -1:
        return 0

    last = binary_search(a, k, 0, len(a) - 1, "last")
    return last - first + 1


def binary_search(a, k, left, right, search_type):

    if not a or left > right:
        return -1

    mid = left + (right - left) // 2

    if a[mid] == k:

        if search_type == "first":
            if mid - 1 >= 0 and a[mid-1] == k:
                return binary_search(a, k, left, mid - 1, search_type)

        if search_type == "last":
            if mid + 1 < len(a) and a[mid + 1] == k:
                return binary_search(a, k, mid + 1, right, search_type)

        return mid
    elif a[mid] < k:
        return binary_search(a, k, mid + 1, right, search_type)
    else:
        return binary_search(a, k, left, mid - 1, search_type)

    #return -1

a = [1, 1, 1, 2, 3]
k = 1

result = total_occurances(a, k)

print(result)

a = [1, 1, 1, 2, 3]
k = 4

result = total_occurances(a, k)

print(result)

a = [1, 1, 1, 2, 3, 5, 6, 7, 7, 7, 7, 7, 8, 9]
k = 7

result = total_occurances(a, k)

print(result)