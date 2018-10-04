# -*- coding:utf-8 -*-
# 这题没意思，用系统自带函数了。。
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        try:
            a = float(s)
            return True
        except:
            return False