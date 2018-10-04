# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.dic = {}
        self.s = ''
        
    def FirstAppearingOnce(self):
        # write code here
        for key in self.s:
            if self.dic[key] == 1:
                return key
        return '#'
        
    def Insert(self, char):
        # write code here
        self.dic[char] = 1 if char not in self.dic else self.dic[char]+1
        self.s += char