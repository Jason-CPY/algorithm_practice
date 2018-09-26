# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.li = []
        self.res = []
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return self.res
        self.li.append(root.val)
        expectNumber -= root.val
        if expectNumber == 0 and not root.left and not root.right:
            self.res.append(self.li[:])
        self.FindPath(root.left,expectNumber)
        self.FindPath(root.right,expectNumber)
        self.li.pop()
        return self.res