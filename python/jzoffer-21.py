# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        l = []
        low = 0
        while popV:
            if l and l[-1] == popV[0]:
                popV.pop(0)
                l.pop()
            elif pushV:
                l.append(pushV.pop(0))
            else:
                return False
        return True