# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
223: Rectangle Area
https://leetcode.com/problems/rectangle-area/

Find the total area covered by two rectilinear rectangles in a 2D plane.
Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
Assume that the total area is never beyond the maximum possible value of int.

=== Comments by Dabay===
S(M ∪ N) = S(M) + S(N) - S(M ∩ N)
'''

class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        a1 = (C - A) * (D - B)
        a2 = (G - E) * (H - F)
        cross = max(min(C, G) - max(A, E), 0) * max((min(D, H) - max(B, F), 0))
        return a1 + a2 - cross


def main():
    sol = Solution()
    print sol.computeArea(-3,0,3,4,0,-1,9,2)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)