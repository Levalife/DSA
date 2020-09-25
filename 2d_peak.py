# -*- coding: utf-8 -*-


def peak_2d(a):
    while True:
        m = len(a[0])
        j = m // 2
        max = 0
        for i in range(1, len(a)):
            if a[i][j] > a[max][j]:
                max = i

        if len(a[0]) == 1:
            return a[max][j]
        elif a[max][j] < a[max][j - 1]:  # если j - 1 больше чем j то значения уже спадают и пик был слева, берем левые стобцы
            a = [b[:j] for b in a]
        elif a[max][j] < a[max][j+1]: # если j + 1 больше чем j то значения только наростают и пик справа
            a = [b[j + 1:] for b in a]

b = [[1,2,10,3],
     [14,13,12,5],
     [15,9,11,17],
     [16,17,19,20]]

c = [[1,2,10,3,2],
     [14,13,12,5,5],
     [15,9,11,17,16],
     [16,17,19,20,15]]

d = [[1,2,10,3,2],
     [16,17,19,20,15],
     [14,13,12,5,5],
     [15,9,11,17,16]]


e = [[14,13,12,5,5],
     [16,17,19,20,15],
     [1,2,10,3,2],
     [15,9,11,17,16]]

# print(peak_2d(b))
# print(peak_2d(c))
# print(peak_2d(d))


def greedy_peak_2d(a):
    i = len(a) // 2
    j = len(a[0]) // 2
    while True:
        print(a[i][j], end=' -> ')
        if j < len(a[0]) - 1 and a[i][j] < a[i][j+1]:
            j = j+1
        elif j > 0 and a[i][j] < a[i][j-1]:
            j = j - 1
        elif i > 0 and a[i][j] < a[i-1][j]:
            i = i - 1
        elif i < len(a) - 1 and a[i][j] < a[i+1][j]:
            i = i + 1
        else:
            print('\n')
            return a[i][j]


print(greedy_peak_2d(b))
print(greedy_peak_2d(c))
print(greedy_peak_2d(d))
print(greedy_peak_2d(e))
