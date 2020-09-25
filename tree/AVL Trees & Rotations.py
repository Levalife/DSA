# -*- coding: utf-8 -*-

'''

Self-Balancing Binary Search Trees

Height = max(LeftSubTreeHeight, RightSubTreeHeight) + 1
Balanced = LeftSubTreeBalance - RightSubTreeBalance
abs(Balance) <= 1 - tree is balanced
Balance  < 0 - tree is left heavy
Balance >= 2 - tree is right heavy

https://www.youtube.com/watch?v=vRwi_UcZGjU&t=3s

1. Handle left heavy tree (Balance  < 0 or LeftSubTreeHeight > 1 + RightSubTreeHeight):
    1.1 Right rotation:
          3                    2
        /                   /   \
       2      ----------> 1     3
      /
    1

         4                      2                       2
        /                        \                    /  \
       2     ----------->         4         ------>  1    4
     /   \                                               /
    1     3                                             3

    Right child of 2 goes as left child of 4

    node = 4
    node.left = 2
    node.left.right = 3

    temp = node.left.right
    node.left.right = node (set 4 as 2 right child)
    node.left = temp (set 3 as 4's left child instead of 2)

    1.2 Left - Right rotation

      3                       3
     /                       /
    1     -------------->   2      ---------> 1.1
     \                     /
      2                   1

2. Handle Right heavy tree (Balance >= 2 or RightSubTreeHeight > 1 + LeftSubTreeHeight):
    2.1 Left rotation:
          1                        2
           \                     /   \
            2   ----------->    1     3
             \
              3


        1                       3                       3
         \                     /                      /   \
          3     -----------> 1        --------->    1       4
        /   \                                        \
       2    4                                         2

       Left child of 3 goes as  right child of 1

       node = 1
       node.right = 3
       node.right.left = 2

       temp = node.right.left
       node.right.left = 1
       node.right = temp

    2.2 Right left rotation

        1               1
         \               \
          3 -------->     2      --------> 2.1
         /                 \
        2                   3
'''