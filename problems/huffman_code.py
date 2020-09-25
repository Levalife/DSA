# -*- coding: utf-8 -*-
import queue as Queue
#Huffman coding assigns variable length codewords to fixed length input characters based on their frequencies.
# More frequent characters are assigned shorter codewords and less frequent characters are assigned longer codewords.
# All edges along the path to a character contain a code digit. If they are on the left side of the tree, they will
# be a 0 (zero). If on the right, they'll be a 1 (one). Only the leaves will contain a letter and its frequency count.
# All other nodes will contain a null instead of a character, and the count of the frequency of all of it and its
# descendant characters.

#For instance, consider the string ABRACADABRA. There are a total of  characters in the string. This number should
# match the count in the ultimately determined root of the tree. Our frequencies are  and . The two smallest frequencies
# are for  and , both equal to , so we'll create a tree with them. The root node will contain the sum of the counts of
# its descendants, in this case . The left node will be the first character encountered, , and the right will contain .
# Next we have  items with a character count of : the tree we just created, the character  and the character .
# The tree came first, so it will go on the left of our new root node.  will go on the right. Repeat until the tree
# is complete, then fill in the 's and 's for the edges. The finished graph looks like:

#Input characters are only present in the leaves. Internal nodes have a character value of ϕ (NULL). We can determine
# that our values for characters are:

#A - 0
#B - 111
#C - 1100
#D - 1101
#R - 10
#Our Huffman encoded string is:

# A B    R  A C     A D     A B    R  A
# 0 111 10 0 1100 0 1101 0 111 10 0
# or
# 01111001100011010111100

# Function Description

# Complete the function decode_huff in the editor below. It must return the decoded string.

cntr = 0


class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count


def huffman_hidden():  # builds the tree and returns root
    q = Queue.PriorityQueue()

    for key in freq:
        q.put((freq[key], key, Node(freq[key], key)))

    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0')
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj))

    root = q.get()
    root = root[2]  # contains root object
    return root


def dfs_hidden(obj, already):
    if (obj == None):
        return
    elif (obj.data != '\0'):
        code_hidden[obj.data] = already

    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")


"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""


def decodeHuff(root, s):
    # Enter Your Code Here
    current = root
    result = ''
    i = 0
    while i < len(s):
        if int(s[i]) == 0:
            current = current.left
        else:
            current = current.right

        if not current.left and not current.right:
            result += current.data
            current = root
        i += 1
    print(result)


ip = input()
freq = {}  # maps each character to its frequency

cntr = 0

for ch in ip:
    if (freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch] += 1

root = huffman_hidden()  # contains root of huffman tree

code_hidden = {}  # contains code for each object

dfs_hidden(root, "")

if len(code_hidden) == 1:  # if there is only one character in the i/p
    for key in code_hidden:
        code_hidden[key] = "0"

toBeDecoded = ""

for ch in ip:
    toBeDecoded += code_hidden[ch]

decodeHuff(root, toBeDecoded)
