# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        l1 = []
        l2 = []
        for i in array:
            if i % 2 == 0 or i == 0:
                l2.append(i)
            else:
                l1.append(i)
        return l1+l2