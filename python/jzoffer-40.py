# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array:
            return []
        tmp = 0
        for i in array:
            tmp ^= i
        num1 = num2 = 0
        cur = 1
        while cur & tmp == 0:
            cur <<= 1
        for num in array:
            if num & cur == 0:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]