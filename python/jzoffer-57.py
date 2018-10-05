# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        dummy = pNode
        while dummy.next:
            dummy = dummy.next
        self.result = []
        self.midTraversal(dummy)
        return self.result[self.result.index(pNode) + 1] if self.result.index(pNode) != len(self.result) - 1 else None
        
    def midTraversal(self, root):
        if not root: return
        self.midTraversal(root.left)
        self.result.append(root)
        self.midTraversal(root.right)