# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return 0
        numlist = [1]
        i2 = i3 = i5 = 0
        num = 0
        while len(numlist) < index:
            num2 , num3, num5 = numlist[i2] * 2, numlist[i3] * 3, numlist[i5] * 5
            num = min(num2, num3, num5)
            if num == num2:
                i2 += 1
            if num == num3:
                i3 += 1
            if num == num5:
                i5 += 1
            numlist.append(num)
        return numlist[-1]