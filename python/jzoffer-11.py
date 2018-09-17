# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        cnt = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            n = n & (n - 1)
            cnt += 1
        return cnt