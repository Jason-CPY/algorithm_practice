# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        g = -10000000000
        l = -10000000000
        for n in array:
            g = max(n,n+g)
            l = max(g,l)
        return l