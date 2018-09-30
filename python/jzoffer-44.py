# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if s.split() == []:
            return s
        return " ".join(s.split()[::-1])