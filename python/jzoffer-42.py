# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        res = []
        i = 0
        j = len(array) - 1
        while i < j:
            if array[i] + array[j] == tsum:
                res.append(array[i])
                res.append(array[j])
                break
            while i < j and array[i] + array[j] > tsum:
                j -= 1
            while i < j and array[i] + array[j] < tsum:
                i += 1
        return res