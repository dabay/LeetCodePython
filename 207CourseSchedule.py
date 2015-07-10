# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
207: Course Schedule
https://leetcode.com/problems/course-schedule/

There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs,
is it possible for you to finish all courses?

For example:
2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0,
and to take course 0 you should also have finished course 1. So it is impossible.

=== Comments by Dabay===
拓扑排序
用hash来记录，key是课程编号，value是一个list，其中第一个有多少课程依赖与它；第二个是它依赖于哪些课程。
'''

class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        courses = {}
        for i in xrange(numCourses):
            courses[i] = [0,[]]
        for c1, c2 in prerequisites:
            courses[c2][0] += 1
            courses[c1][1].append(c2)

        zero_in_course = self.zero_in(courses)
        while zero_in_course is not None:
            for out in zero_in_course[1]:
                courses[out][0] -= 1
            zero_in_course = self.zero_in(courses)
        return len(courses) == 0

    def zero_in(self, courses):
        for k in courses:
            if courses[k][0] == 0:
                outs = courses[k][1]
                del courses[k]
                return (k, outs)
        else:
            return None




def main():
    num = 2
    prerequisites = []
    sol = Solution()
    print sol.canFinish(num, prerequisites)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)