# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

31: Next Permutation
https://oj.leetcode.com/problems/next-permutation/

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

===Comments by Dabay===

比如 5 9 8 4 2 1
从末尾1开始往前面看，知道升序结束。在【9 8 4 2 1】中找一个正好比5大的数8，交换变成8 9 5 4 2 1。
然后把 【9 5 4 2 1】反转，变成【1 2 4 5 9】。最后结果为： 8 1 2 4 5 9


'''

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        i = len(num) - 1
        while i > 0:
            if num[i-1] >= num[i]:
                i -= 1
                continue
            j = i
            while j < len(num):
                if num[j] > num[i-1]:
                    j += 1
                    continue
                break
            num[i-1], num[j-1] = num[j-1], num[i-1]
            tails = num[i:]
            tails.reverse()
            return num[:i] + tails
        else:
            num.reverse()
            return num


def main():
    s = Solution()
    nums = [5, 1, 1]
    print s.nextPermutation(nums)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)