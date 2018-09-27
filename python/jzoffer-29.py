# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k > len(tinput):
            return []
        self.quick_sort(tinput, 0, len(tinput)-1)
        return tinput[:k]
        
    def quick_sort(self, array, left, right):
        if left > right:
            return
        low = left
        high = right
        key = array[low]
        while left < right:
            while left < right and array[right] >= key:
                right -= 1
            array[left] = array[right]
            while  left < right and array[left] < key:
                left += 1
            array[right] = array[left]
        array[left] = key
        self.quick_sort(array,low,left - 1)
        self.quick_sort(array,left + 1,high)