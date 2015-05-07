# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'

204: Count Primes
https://leetcode.com/problems/count-primes/

Count the number of prime numbers less than a non-negative number, n

=== Comments by Dabay===
计算质数的总数。需要用空间来换一些时间，不然下面的代码过不了。
if n == 1:
    return 0
if n == 2:
    return 1
primes = [2]
for x in xrange(3, n):
    for p in primes:
        if x % p == 0:
            break
    else:
        primes.append(x)
else:
    return len(primes)
'''

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <= 2:
            return 0
        matrix = [False for _ in xrange(n)]
        matrix[0] = True    # 1不是质数
        primes = []
        for i in xrange(1, n-1):
            if matrix[i] == True:
                continue
            p = i + 1
            primes.append(p)
            c = n / p
            for x in xrange(2, c+1):
                matrix[p*x-1] = True
        else:
            return len(primes)



def main():
    sol = Solution()
    print sol.countPrimes(2)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)