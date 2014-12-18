# -*- coding: utf8 -*-
'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's,
then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
'''

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        def jump(A, index, jump_to):
            to_insert = A[index]
            for i in xrange(jump_to, index + 1):
                (A[i], to_insert) = (to_insert, A[i])


        last_0_index = -1
        last_1_index = -1
        for i in xrange(len(A)):
            if A[i] == 0:
                jump(A, i, last_0_index + 1)
                last_0_index = last_0_index + 1
                last_1_index = last_1_index + 1
            elif A[i] == 1:
                jump(A, i, last_1_index + 1)
                last_1_index = last_1_index + 1
            else:
                continue


if __name__ == "__main__":
    s = Solution()
    color_list = [0,1,2,0,1,0,2,0]
    s.sortColors(color_list)
    print color_list




  
