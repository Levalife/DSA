'''

 11
+ 1
100


XOR (exclusive or)
 11                                             1 1 0 0
 01                                             1 0 1 0
 10  -- imitates addition without carry         0 1 1 0

& AND
 11
 01
 01  -- imitates positions where carry appear but needs to be shifted to the left to be applied

 01
<<
 10

If combine XOR, with AND and << we can get immitation of addition
'''

def add(a, b):

    while True:
        #find carry with the help of AND andleft shift
        carry = (a & b) << 1

        #imitate addition with XOR
        a = a ^ b

        # set carry to be and repeat operation  sequence while carry will not be equal to 0
        b = carry

        if carry == 0:
            break
    return a


print(add(3, 1))