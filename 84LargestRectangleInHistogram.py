# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

84: Largest Rectangle in Histogram
https://oj.leetcode.com/problems/largest-rectangle-in-histogram/

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.

===Comments by Dabay===
http://www.tuicool.com/articles/7zUvmy
O(N)的解法，不服不行。
注意几个细节：
    - 栈中存储下标（栈中的元素对应的高度从低到高）
    - 为了能让全部出栈，在height后面加一个元素0
    - 如果出栈一个元素之后
        -   栈为空，说明这个下标对应的高度最矮的，其宽度应该是下标0到i-1，即i
        -   栈不为空，说明前面有更矮的，这里只需要计算local peak冒出来的一部分即可
'''

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        largest = 0
        stack = [0]
        i = 1
        height.append(0)
        while i < len(height):
            while len(stack)>0 and height[stack[-1]] > height[i]:
                index = stack.pop()
                h = height[index]
                if len(stack) == 0:
                    area = i * h
                else:
                    area = (i-1-stack[-1])*h
                largest = max(largest, area)
            else:
                stack.append(i)
                i += 1
        return largest


def main():
    sol = Solution()
    height = [0,3,2,5]
    print sol.largestRectangleArea(height)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
