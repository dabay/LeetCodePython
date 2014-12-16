# -*- coding: utf8 -*-
'''
Compare two version numbers version1 and version1.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a boolean
    def compareVersion(self, version1, version2):
        v1 = version1.split(".")
        v2 = version2.split(".")
        if len(v1) > len(v2):
            for i in xrange(len(v1)-len(v2)):
                v2.append("0")
        elif len(v2) > len(v1):
            for i in xrange(len(v2)-len(v1)):
                v1.append("0")

        for index in xrange(len(v1)):
            ver1 = int(v1[index])
            ver2 = int(v2[index])
            if ver1 > ver2:
                return 1
            elif ver1 < ver2:
                return -1

        return 0


if __name__ == "__main__":
    s = Solution()
    print s.compareVersion("1", "1.1")






  
