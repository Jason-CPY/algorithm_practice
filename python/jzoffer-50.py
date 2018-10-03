# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:
            return False
        numbers.sort()
        for i,v in enumerate(numbers[:-1]):
            if v == numbers[i+1]:
                duplication[0] = v
                return True
        return False