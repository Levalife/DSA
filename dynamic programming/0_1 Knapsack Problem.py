'''

0/1 Knapsack Problem

DYNAMIC PROGRAMMING

https://www.youtube.com/watch?v=xCbYmUPvc2Q

https://www.youtube.com/watch?v=8LusJS5-AGo

Write a program for the knapsack problem that selects a subset of items that has maximum value and satisfies the weight
constraint. All items have integer weights and values. Return the value of the subset.

Build matrix which will have weights items as rows and max weight of knapsack + 1 as columns

weights = {
    5: 60,
    3: 50,
    4: 70,
    2: 30
}

max_weight = 5

Resolve subproblems: what item on every step will we choose and what not. Step by step from first item (5 kg) and first
max weight of knapsack (0 kg)

If item weight > current max weight - set 0 (if now previous items are choosen) or choosen previously (i - 1)
If weight => current max - choose which combination will suit better - previously choosen items (i - 1, j) or
current item + previously choosen item that fits into left weight (j - current weight)

            0   1   2   3   4   5
5 kg (60)   0   0   0   0   0   60
3 kg (50)   0   0   0   50  50  60
4 kg (70)   0   0   0   50  70  70
2 kg (30)   0   0   30  50  70  80  <--- answer


'''

def knapsack(weights, max_weight):

    result = []

    for _ in weights.keys():
        result.append([0] * (max_weight + 1))

    for i, weight in enumerate(weights.keys()):
        for j in range(1, max_weight + 1):
            if weight > j:
                if i > 0:
                    result[i][j] = result[i - 1][j]
                else:
                    result[i][j] = 0
            else:
                if i > 0:

                    result[i][j] = max(weights[weight] + result[i - 1][j - weight] if j - weight >= 0 else 0,
                                       result[i - 1][j])
                else:
                    result[i][j] = weights[weight]

    return result[-1][-1]

weights = {
    5: 60,
    3: 50,
    4: 70,
    2: 30
}

max_weight = 5

result = knapsack(weights, max_weight)
print(result)

weights = {
    1: 1,
    3: 4,
    4: 5,
    5: 7
}

max_weight = 7

result = knapsack(weights, max_weight)
print(result)