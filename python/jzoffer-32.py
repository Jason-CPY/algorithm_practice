# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        numbers = list(map(str,numbers))
        l = lambda n1,n2:int(n1+n2)-int(n2+n1)
        numbers = sorted(numbers,cmp=l)
        return "".join(i for i in numbers)