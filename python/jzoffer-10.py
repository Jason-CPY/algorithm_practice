# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        x,a,b = 0,0,1
        while x < number:
            a,b = b,a+b
            x += 1
        return b