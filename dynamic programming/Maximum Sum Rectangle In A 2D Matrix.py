'''

https://www.youtube.com/watch?v=-FgseNO-6Gk

Kadane's Algorithm

'''

def maxRectungleSum(rect):
    row_sum = [0] * len(rect)
    l = 0
    r = 0
    max_rect_sum = rect[0][0]

    while l < len(rect):
        for i in range(len(rect)):
            row_sum[i] = rect[l][i]

        while r < len(rect):
            for i in range(len(rect)):
                row_sum[i] = sum(rect[i][l: r + 1])
            r += 1
            max_rect_sum = max(max_rect_sum, maxSumInRow(row_sum))

        l += 1
        r = l
    return max_rect_sum


def maxSumInRow(row):
    max_sum = row[0]
    for i in range(1, len(row)):
        max_sum = max(max_sum + row[i], row[i])
    return max_sum

a = [
    [6, -5, -7, 4, -4],
    [-9, 3, -6, 5, 2],
    [-10, 4, 7, -6, 3],
    [-8, 9, -3, 3, 7]
]

result = maxRectungleSum(a)
print(result)