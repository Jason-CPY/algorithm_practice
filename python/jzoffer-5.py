# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.l1 = []
        self.l2 = []
    def push(self, node):
        # write code here
        while self.l2:
            self.l1.append(self.l2.pop())
        self.l1.append(node)
    def pop(self):
        # return xx
        while self.l1:
            self.l2.append(self.l1.pop())
        return self.l2.pop()