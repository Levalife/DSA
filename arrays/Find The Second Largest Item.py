'''

Min HEAP approach or TWO POINTERS approach

https://www.youtube.com/watch?v=NheWPxGpoxQ

Min Heap approach:
create heap size 2
add to the heap only elements greater then root element
support len == 2 by deleting root element after insertions, if needed

so you will end up with second largest element in the root and largest element in the leaf

Two Pointer Approach:
Set to pointers max1 and max2
Iterate through array: if element > than max1 : max2 = max1, max1 = element
                       else if element > than max2 and not equal to max1 (so we won't end up with equal numbers
                       as largest and second largest elements): max2 = element

'''

a = [-1, 10, 8, 9, 10, 9, -8, 11]

def second_largest(a):

    max1 = a[0]
    max2 = a[1]

    for i in range(1, len(a)):
        if a[i] > max1:
            max2 = max1
            max1 = a[i]
        else:
            if a[i] > max1 and a[i] != max1:
                max2 = a[i]
    return max2

print(second_largest(a))