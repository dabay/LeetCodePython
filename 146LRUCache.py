# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

146: LRU Cache
https://leetcode.com/problems/lru-cache/

Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present.
    When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

=== Comments by Dabay===

'''

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.space = capacity
        self.dict = {}
        self.queue = []

    # @return an integer
    def get(self, key):
        if key not in self.dict.keys():
            return -1
        self.queue.remove(key)
        self.queue.append(key)
        return self.dict[key]

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.dict.keys():
            self.dict[key] = value
            self.queue.remove(key)
            self.queue.append(key)
        else:
            if len(self.dict) < self.space:
                self.dict[key] = value
                self.queue.append(key)
            else:
                old_key = self.queue.pop(0)
                self.dict.pop(old_key)
                self.dict[key] = value
                self.queue.append(key)


def main():
    cache = LRUCache(2)
    cache.set(2, 1)
    cache.set(2, 2)
    print cache.get(2)
    cache.set(1, 1)
    cache.set(4, 1)
    print cache.get(2)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
