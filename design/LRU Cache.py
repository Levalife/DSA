'''

In python 3.7 dict is ordered so we can use dict for least recent cache. Least recent elements would be at the end of
the dict, so overhead would be deleted from the head (beginning) of the dict

For lower version of python we can use Ordered Dict or complex structures as:

hashtable (dict) for quick search
doubly linked list for quick access and delition (with dummy head and dummy tail for quick insertion and deletion of
the overhead)

https://leetcode.com/problems/lru-cache/

https://www.youtube.com/watch?v=S6IfqDXWa10

'''


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            val = self.cache.pop(key)
            self.cache[key] = val # will be inserted at the and

        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        else:
            if len(self.cache) == self.capacity:
                # will be deleted from the beginning
                del self.cache[next(iter(self.cache))]

        self.cache[key] = value # will be inserted at the and

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)