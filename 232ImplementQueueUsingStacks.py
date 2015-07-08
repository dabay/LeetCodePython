# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
232: Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/

 Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.

Notes:

    You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size,
    and is empty operations are valid.
    Depending on your language, stack may not be supported natively.
    You may simulate a stack by using a list or deque (double-ended queue),
    as long as you use only standard operations of a stack.
    You may assume that all operations are valid
    (for example, no pop or peek operations will be called on an empty queue).

=== Comments by Dabay===
维护两个stack
'''

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack1.append(x)

    # @return nothing
    def pop(self):
        if len(self.stack1) == 0:
            return None
        if len(self.stack1) == 1:
            return self.stack1.pop(-1)
        while self.stack1:
            self.stack2.append(self.stack1.pop(-1))
        res = self.stack2.pop(-1)
        while self.stack2:
            self.stack1.append(self.stack2.pop(-1))
        return res

    # @return an integer
    def peek(self):
        if len(self.stack1) == 0:
            return None
        if len(self.stack1) == 1:
            return self.stack1[-1]
        while self.stack1:
            self.stack2.append(self.stack1.pop(-1))
        res = self.stack2[-1]
        while self.stack2:
            self.stack1.append(self.stack2.pop(-1))
        return res


    # @return an boolean
    def empty(self):
        return len(self.stack1) == 0


def main():
    q = Queue()
    q.push(1)
    q.push(2)
    print q.pop()


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)