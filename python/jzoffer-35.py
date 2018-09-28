# -*- coding:utf-8 -*-
#没通过，超时了
class Solution:
    def InversePairs(self, data):
        # write code here
        count = 0
        copy = data[:]
        copy.sort()
        l = len(copy)
        for i in range(l):
            count += data.index(copy[i])
            data.remove(copy[i])
        return count%1000000007