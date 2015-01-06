# -*- coding: utf8 -*-
'''
https://oj.leetcode.com/problems/gas-station/

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
'''

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        def canComplateCircuit2(gas, cost):
            left = gas[0] - cost[0]
            for i in xrange(1, len(gas)):
                if left < 0:
                    return False
                left = left + gas[i] - cost[i]
            if left < 0:
                return False
            else:
                return True

        for i in xrange(len(gas)):
            if gas[i] < cost[i]:
                continue
            if canComplateCircuit2(gas[i:] + gas[:i], cost[i:] + cost[:i]):
                return i
        return -1


def main():
    s = Solution()
    print s.canCompleteCircuit([2, 3], [3, 2])


if __name__ == "__main__":
    import time
    starttime = time.clock()
    main()
    endtime = time.clock()
    print "%s sec" % (endtime - starttime)