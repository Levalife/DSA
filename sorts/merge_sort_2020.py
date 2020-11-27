


def merge(a):

    if len(a) <= 1:
        return a

    mid = len(a) // 2

    left = merge(a[:mid])
    right = merge(a[mid:])

    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < len(left):
        result.extend(left[i:])

    if j < len(right):
        result.extend(right[j:])

    return result

a = [2, 4, 1, 7,8, -9, 10, 5, 3, 0]

result = merge(a)
print(result)