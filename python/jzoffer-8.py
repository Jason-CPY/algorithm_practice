# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 0:
            return 0
        x,a,b = 0,0,1
        while x < number:
            a,b = b,a+b
            x+=1
        return b