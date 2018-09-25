# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        q = [root]
        res = []
        while q:
            current = q.pop(0)
            res.append(current.val)
            if current.left != None:
                q.append(current.left)
            if current.right != None:
                q.append(current.right)
        return res