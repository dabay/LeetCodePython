# -*- coding: utf8 -*-
'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x < 0:
            return -1
        if x == 0:
            return 0
        if x == 1:
            return 1
        ceiling = x
        floor = 1
        while ceiling > floor:
            s = (ceiling + floor) / 2
            s2 = s * s
            if s2 == x:
                return s
            elif s2 > x:
                if s < ceiling:
                    ceiling = s
                else:
                    ceiling = ceiling - 1
                    if floor == ceiling:
                        return floor
                continue
            else:
                if s > floor:
                    floor = s
                else:
                    floor = floor + 1
                    if floor == ceiling:
                        return floor - 1
                continue


if __name__ == "__main__":
    s = Solution()
    print s.sqrt(2)



  
