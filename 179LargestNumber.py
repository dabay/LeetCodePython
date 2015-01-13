# -*- coding: utf8 -*-
'''
__author__ = 'dabay.wang@gmail.com'
https://oj.leetcode.com/problems/largest-number/

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

===Comments by Dabay===
把所有num都存到一个hash表中，用值来记录出现的次数。
对于，num中很多重复项来说，这样的处理可以节约时间。

定义比较的方法：当把两个字符串长度不一样时，把他们互相加到末尾比较。
'''
class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        def compare(num1, num2):
            if len(num1) != len(num2):
                num1,num2 = num1 + num2,num2 + num1
            return [-1, 1][num1 > num2]

        d = {}
        for n in num:
            n = str(n)
            if n not in d:
                d[n] = 1
            else:
                d[n] = d[n] + 1

        keys = d.keys()
        keys = sorted(keys, cmp=compare, reverse=True)

        result = ""
        for k in keys:
            result = result + str(k) * d[k]

        result = result.lstrip('0')
        if len(result) == 0:
            return "0"
        else:
            return result


def main():
    s = Solution()
    nums = [3, 30, 34, 5, 9]
    nums = [6306,9385,7536,3462,4798,5422,5529,8070,6241,9094,7846,663,6221,216,6758,8353,3650,3836,8183,3516,5909,6744,1548,5712,2281,3664,7100,6698,7321,4980,8937,3163,5784,3298,9890,1090,7605,1380,1147,1495,3699,9448,5208,9456,3846,3567,6856,2000,3575,7205,2697,5972,7471,1763,1143,1417,6038,2313,6554,9026,8107,9827,7982,9685,3905,8939,1048,282,7423,6327,2970,4453,5460,3399,9533,914,3932,192,3084,6806,273,4283,2060,5682,2,2362,4812,7032,810,2465,6511,213,2362,3021,2745,36368398,6265,1518,100,9051,5526,2264,5041,1630,5906,6787,8382,4662,4532,6804,4710,4542,2116,7219,8701,8308,957,8775,4822,396,8995,8597,2304,8902,830,8591,5828,9642,7100,3976,5565,5490,1613,5731,8052,8985,2623,6325,3723,5224,8274,4787,6310,3393,78,3288,7584,7440,5752,351,4555,7265,9959,3866,9854,2709,5817,7272,43,1014,7527,3946,4289,1272,5213,710,1603,2436,8823,5228,2581,771,3700,2109,5638,3402,3910,871,5441,6861,9556,1089,4088,2788,9632,6822,6145,5137,236,683,2869,9525,8161,8374,2439,6028,7813,6406,7519,100,2732,3229,7875,843,7703,694,8649,881,1980,4091,9504,9154,8562,6744,2481,3168,8532,1057,6485,4437,5295,4174,5121,9577,7835,8900,8898,4549,2523,1338,3576,1815,2788,7231,923,4404,7448,2852,9394,8969,6003,8314,8004,8871,9885,1381,691,8465,370,1337,8946,5740,5069,2336,5239,9604,9288,8289,9117,2554,323,8491,7969,8591,644,6469,3856,2176,2812,8537,6105,710,7486,497,5103,3675,2311,9878,2778,7828,143,7873,4826,3188,7218,7061,2181,3368,7373,8252,4100,4421,3965,5895,3968,3636,48449653,9943,1695,100,1681,6528,2738,8631,8709,3084,9759,6473,3576,5358,645,8556,871,9114,5708,3300,8780,8693,6569,9455,5296,3388,3617,8270,9674,7090,8535,3340,4483,5354,3410,3916,6996,1942,4957,4825,5501,7490,9810,7747,7496,9657,1934,6540,1693,3722,6950,9766,5213,724,4727,1793,7173,9086,9574,250,9901,829,9116,390,4299,1208,726,6251,3834,2785,3400,5080,8791,5606,6275,1093,3091,1673,8271,7434,226,5505,5886,9552,9098,8164,1701,2675,3463,4564,187,1042,2686,2676,5313,4072,7443,5412,8389,3182,653,4341,1299,447,100,2331,9511,5618,6542,2387,7224,5955,9267,8454,4178,4399,183,3314,6191,3993,9334,5608,5610,5123,3649,6003,8321,67443923,5974,1849,7250,6533,7960,7968,9034,1568,9209,1358,3920,5422,203,468,7441,435,9277,1984,7326,9044,3398,1501,2139,1991,6612,2039,184,2666,4648,7896,5698,352,7319,7546,5654,440,4755,4365,6702,8568,9949,49,5235,7306,1870,4667,6787,9866,6188,9836,1970,8424,473,1345,275,8634,7553,9971,2085,9910,9602,8960,5917,6795,3822,883,224,5012,8353,8529,8423,9679,6096,5501,6116,1245,100,5041,7233,8441,8543,6385,3510,7485,8082,2331,4285,1741,6090,5940,9375,1881,2398,8853,4536,5570,2602,670,3797,877,485,5293,2977,9745,6911,7724,6942,1018,5538,5975,814,8040,3729,8109,6632,7401,6251,9316,1160,3350,6454,169,9043,9985,9739,6648,8383,310,6228,9760,1091,2377,4596,4072,5725,5711,236,9743,9579,1136,707,4622,2247,230,6623,4310,1516,7388,1595,2204,1331,3109,4307,5117,6790,9996,3248,2877,7770,7156,6088,3034,3229,9354,6063,9388,2030,6176,3521,9438,3329,2533,2184,1247,7002,844,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161,3161]
    #nums = [0, 0]
    print s.largestNumber(nums)


if __name__ == "__main__":
    import time
    start = time.clock()
    main()
    print "%s sec" % (time.clock() - start)
