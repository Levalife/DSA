

def sink_up(heap):
    index = len(heap) - 1
    parent = (index - 1) // 2
    while index > 0 and heap[index] > heap[parent]:
        heap[index], heap[parent] = heap[parent], heap[index]
        index = parent
        parent = (index - 1) // 2


def sink_down(heap):
    index = 0
    n = len(heap)
    left = 2 * index + 1
    right = 2 * index + 2
    flag = True
    while left < n and flag:

        if right >= n:
            maxIndex = left
        else:
            if heap[right] > heap[left]:
                maxIndex = right
            else:
                maxIndex = left

        if heap[index] < heap[maxIndex]:
            heap[index], heap[maxIndex] = heap[maxIndex], heap[index]
            index = maxIndex
            left = 2 * index + 1
            right = 2 * index + 2
        else:
            flag = False

    return heap


def heap_sort(array):

    heap = []
    for el in array:
        heap.append(el)
        sink_up(heap)

    result = []
    n = len(heap)
    while n > 1:
        result.append(heap[0])
        heap[0] = heap[-1]
        heap = sink_down(heap[:n-1])

        n = n - 1
    return result

a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print(heap_sort(a))