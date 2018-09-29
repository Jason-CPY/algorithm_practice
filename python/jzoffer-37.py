# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return self.search(data, k+0.5)-self.search(data, k-0.5)
    
    def search(self, data, n):
        s = 0
        l = len(data) - 1
        while s <= l:
            mid = (s + l)/2
            if data[mid] < n:
                s = mid + 1
            else:
                l = mid - 1
        return s