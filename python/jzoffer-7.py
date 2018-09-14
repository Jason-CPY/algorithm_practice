# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        x,a,b = 1,0,1
        while x < n:
            a,b = b,a+b
            x+=1
        return b