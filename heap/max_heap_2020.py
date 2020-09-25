# -*- coding: utf-8 -*-


a = [16, 10, 14, 9, 8, 7,  4 , 3 ,2, 1]


def insert_heap(heap, el):

    heap.append(el)
    return sink_up(heap)


def delete_node(heap, ):

    heap[0], temp = heap[-1], heap[0]

    heap.pop()

    sink_down(heap)
    print(temp)
    return temp


def sink_up(heap):
    n = len(heap)
    index = n - 1
    parent = (index - 1) // 2

    while index > 0 and heap[parent] < heap[index]:
        parent = (index - 1) // 2
        if heap[index] > heap[parent]:
            heap[index], heap[parent] = heap[parent], heap[index]
            index = parent
            parent = (index - 1) // 2
    return heap


def sink_down(heap):
    index = 0
    left = 2 * index + 1
    right = 2 * index + 2
    n = len(heap)
    flag = True
    while left < n and flag:
        print(left, n)
        if right >= n:
            maxIndex = left
        else:
            if heap[left] > heap[right]:
                maxIndex = left
            else:
                maxIndex = right
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
    for e in array:
        heap.append(e)
        sink_up(heap)
    print("Max heap", heap)
    result = []
    while len(heap) > 0:

        result.append(delete_node(heap))
        print(result)

    return result[::-1]


def heapify(array):

    '''
        Iterate through the array from the end

        Compare with children
        Sink down if lower then children

        n//2 because n//2 is leafs without children and n//2 leafs with children

    '''

    n = len(array)
    for a in range(n//2, -1, -1):
        index = a

        array[a:] = sink_down(array[a:])
    return array


#print(insert_heap(a, 11))
#a = insert_heap(a, 11)
#print(a)
#print(delete_node(a, len(a)))
a =  [16, 14, 10, 8, 7, 3, 9, 1, 4, 2]
#print(delete_node(a))


a = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
#print(heap_sort(a))
print(heapify(a))
# [16, 11, 14, 9, 10, 7, 4, 3, 2, 1, 8]
# [16, 11, 14, 9, 10, 7, 4, 3, 2, 1, 8]
# [14, 11, 8, 9, 10, 7, 4, 3, 2, 1]
# [11, 10, 8, 9, 1, 7, 4, 3, 2]

# if __name__ == '__main__':
#     a1 = [4, 14, 7, 2, 8, 1]
#     print(max_heapify(a1, 0))
#
#     a2 = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
#     print(build_max_heap(a2))
#
#     a3 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
#     print(build_max_heap(a3))
#
#     a1 = [4, 14, 7, 2, 8, 1]
#     print(max_heapify_req(a1, 0))
#     a2 = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
#     print(build_max_heap_with_req(a2))
#
#     a3 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
#     print(build_max_heap_with_req(a3))