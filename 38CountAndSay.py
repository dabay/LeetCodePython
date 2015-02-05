# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

38: Count and Say
https://oj.leetcode.com/problems/count-and-say/

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
Note: The sequence of integers will be represented as a string.

===Comments by Dabay===
题意半天没搞懂。原来是给的数字n是几，就返回第几个字符串。例如，如果n是5，就返回“111221”这个字符串。
第一个铁定是1，然后用say的方式来往后生成下一个字符串。

say的时候：
比较下一个数字是否一样，
    如果一样，计数器加一
    如果不一样，say
'''

class Solution:
    # @return a string
    def countAndSay(self, n):
        current_result = "1"
        start = 1
        while start < n:
            previous_result = current_result
            current_result = ""
            counting_number = None
            counter = 0
            for num in previous_result:
                if counting_number is None:
                    counting_number = num
                    counter = 1
                elif counting_number == num:
                    counter += 1
                else:
                    current_result += "%s%s" % (counter, counting_number)
                    counting_number = num
                    counter = 1
            else:
                current_result += "%s%s" % (counter, counting_number)
            start += 1
        return current_result


def main():
    sol = Solution()
    print sol.countAndSay(5)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)




