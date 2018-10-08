# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.arr = []
        
    def Insert(self, num):
        # write code here
        self.arr.append(num)
        self.arr.sort()
        
    def GetMedian(self, noone):
        # write code here
        l=len(self.arr)
        if l % 2 == 1:
            return self.arr[l/2]
        return (self.arr[l/2] + self.arr[l/2 - 1])/2.0