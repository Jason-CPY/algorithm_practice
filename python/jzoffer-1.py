# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        a = len(array)
        b = len(array[0])
        if a == 0 or b == 0:
            return False
        if target < array[0][0]:
            return False
        if target > array[a-1][b-1]:
            return False
        for i in range(1,a+1):
            if target >= array[a-i][0]:
                for j in range(b):
                    if target == array[a-i][j]:
                        return True
        return False