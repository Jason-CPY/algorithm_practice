# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        p = ListNode(-1)
        p.next = pHead
        p1 = p
        p2 = pHead
        n = None
        while p2 and p2.next:
            n = p2.next
            if p2.val == n.val:
                while n and p2.val == n.val:
                    n = n.next
                p1.next = n
                p2 = n
            else:
                p1 = p2
                p2 = p2.next
        return p.next