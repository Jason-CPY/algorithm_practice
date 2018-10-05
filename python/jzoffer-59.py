# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot: 
            return []
        res = []
        self.level(pRoot, 0, res)
        for level in range(1, len(res), 2):
            res[level] = res[level][::-1]
        return res

    def level(self, root, level, res):
        if not root: 
            return
        if level == len(res):
            res.append([])
        res[level].append(root.val)
        if root.left:
            self.level(root.left, level + 1, res)
        if root.right:
            self.level(root.right, level + 1, res)