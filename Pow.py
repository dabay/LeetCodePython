# -*- coding: utf8 -*-
'''
Implement pow(x, n).
'''

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == 2:
            return x * x
        j = n/2
        k = n - j
        return pow(x, j) * pow(x, k)


if __name__ == "__main__":
    s = Solution()
    print s.pow(8.88023, 3)

  
