# -*- coding: utf8 -*-
'''
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
'''

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        factorial = 1
        for i in xrange(2, n+1):
            factorial = factorial * i
        print factorial
        result = ""

        number_list = []
        for i in xrange(1, n+1):
            number_list.append(str(i))

        i = 1
        mod = k-1
        for i in xrange(1, n+1):
            factorial = factorial / (n-(i-1))
            index = mod / factorial
            result = result + number_list[index]
            number_list.pop(index)
            mod = mod % factorial

        return result


if __name__ == "__main__":
    s = Solution()
    print s.getPermutation(3, 1)

  
