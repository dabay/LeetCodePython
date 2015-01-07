# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/linked-list-cycle-ii/

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?

最好画一个图帮助理解。先用两个指针判断circle，此时快指针走过的路程是慢指针的两倍。
从进入圆环到此时经过了圆环x，慢指针经过的路程就是 从head到进入圆环，再到x。
而快指针经过的路程是，从head到进入圆环，到x，然后再走一圈第二次到x。
所以，快指针多走的1倍距离真好是圆环的周长，也就是head到进入圆环再到x的距离。
此时，让两个指针，以同样的速度，分辨从x和head出发，它们就会在进入圆环的地方相遇。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None:
            return None

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


def main():
    s = Solution()
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n2
    n4.next = n1
    print s.detectCycle(n1).val


if __name__ == "__main__":
    import time
    starttime = time.clock()
    main()
    endtime = time.clock()
    print "%s sec" % (endtime - starttime)