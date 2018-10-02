# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        res = n
        tmp = res and self.Sum_Solution(res - 1)
        res += tmp
        return res