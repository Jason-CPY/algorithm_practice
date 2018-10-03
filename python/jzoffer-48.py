# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        #while num2 > 0:
            #tmp = num1 ^ num2
            #num2 = (num1&num2) << 1
            #num1 = tmp
        # return num1
        #if num2 == 0:
            #return num1
        #return self.Add(num1 ^ num2,(num1&num2)<<1)
        return sum([num1,num2])