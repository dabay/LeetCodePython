# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

85: Maximal Rectangle
https://oj.leetcode.com/problems/maximal-rectangle/

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

===Comments by Dabay===
据说非常经典，牛逼的题目。使用84：Largest Rectangular in Histogram的方法。
注意几个细节：
    - 以每一行为x轴，计算Largest Rectangular
    - 高度是动态规划的，在上次的基础上生成
'''

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        def get_x_list(previous, row):
            i = 0
            while i < len(row):
                if row[i] == "1":
                    previous[i] += 1
                else:
                    previous[i] = 0
                i += 1
            return previous

        def get_largest_rectangular(x_list):
            x_list = list(x_list)
            x_list.append(0)
            stack = []
            largest = 0
            i = 0
            while i < len(x_list):
                if len(stack)>0 and x_list[i] <= x_list[stack[-1]]:
                    while len(stack)>0 and x_list[i] <= x_list[stack[-1]]:
                        x = stack.pop()
                        h = x_list[x]
                        if len(stack) == 0:
                            area = h * i
                        else:
                            area = h * ((x-stack[-1]) + (i-x) - 1)
                        largest = max(largest, area)
                stack.append(i)
                i += 1
            return largest

        if len(matrix) == 0:
            return 0
        x_list = [0 for _ in xrange(len(matrix[0]))]
        maximum = 0
        for row in matrix:
            x_list = get_x_list(x_list, row)
            largest = get_largest_rectangular(x_list)
            maximum = max(maximum, largest)
        return maximum


def main():
    sol = Solution()
    matrix = ["01101","11010","01110","11110","11111","00000"]
    print sol.maximalRectangle(matrix)


if __name__ == '__main__':
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
