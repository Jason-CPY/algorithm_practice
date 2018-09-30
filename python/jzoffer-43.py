# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return s
        if n == len(s):
            return s
        if n > s:
            n = n - len(s)
        return s[n:] + s[:n]