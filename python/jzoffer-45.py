# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        numbers.sort()
        zero_num = numbers.count(0)
        for i,v in enumerate(numbers[:-1]):
            if v != 0:
                if v == numbers[i+1]:
                    return False
                zero_num = zero_num - (numbers[i+1] - v) + 1
                if zero_num < 0:
                    return False
        return True