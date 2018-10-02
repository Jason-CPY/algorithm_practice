# return (self.LastRemaining_Solution(n - 1,m) + m) % n # 超出最大递归深度
# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 1:
            return 0
        if n < 1 or m < 0:
            return -1
        l = range(n)
        start = 0
        final = -1
        while l:
            k = (start + m - 1) % n
            final = l.pop(k)
            n -= 1
            start = k
        return final