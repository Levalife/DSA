'''

https://www.youtube.com/watch?v=gOkNq8Co6B8

Binary search & Reduce Search Space

'''

def findFirstK(a, k):
    l = 0
    r = len(a)
    while True:
        m = (l + r) // 2

        if a[m] == k:

            if m == 0 or a[m - 1] < k:
                return m
            elif a[m - 1] == k:
                r = m - 1
        elif a[m] > k:
            r = m
        else:
            l = m + 1

        if l > r:
            return -1

a = [1, 1, 1, 1, 2, 5, 5, 5, 5, 6, 7, 11]

print(findFirstK(a, 1))
# 0
print(findFirstK(a, 2))
# 4
print(findFirstK(a, 5))
# 5
print(findFirstK(a, 6))
# 9
print(findFirstK(a, 7))
# 10
print(findFirstK(a, 11))
# 11