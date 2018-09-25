# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.l = []
        self.minm = []
    def push(self, node):
        # write code here
        if not self.minm:
            self.minm.append(node)
        else:
            self.minm.append(min(self.minm[-1],node))
        self.l.append(node)
    def pop(self):
        # write code here
        if not self.l:
            return None
        self.minm.pop()
        return self.l.pop()
    def top(self):
        # write code here
        return self.l[-1]
    def min(self):
        # write code here
        if not self.minm:
            return None
        return self.minm[-1]