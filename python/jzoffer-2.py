# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        arr = s.split(' ')
        sp = '%20'
        result = sp.join(arr)
        return result