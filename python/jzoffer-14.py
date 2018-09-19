# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k <= 0:
            return None
        p1 = head
        while k > 1:
            if p1.next:
                p1 = p1.next
                k -= 1
            else:
                return None
        while p1.next:
            p1 = p1.next
            head = head.next
        return head