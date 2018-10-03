# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        numlist=['0','1','2','3','4','5','6','7','8','9','+','-']
        label = 1
        res = 0
        if s == '' or s == '0':
            return 0
        for i in s:
            if i in numlist:
                if i == '+':
                    label = 1
                    continue
                elif i == '-':
                    label = -1
                    continue
                else:
                    res = res*10 + numlist.index(i)
            else:
                return 0
        return res*label