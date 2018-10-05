# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        q = []
        q.append(pRoot)
        res = {}
        level = 0
        current_level_num = 1
        next_level_num = 0
        d = []
        while q:
            current = q.pop(0)
            current_level_num -= 1
            d.append(current.val)
            if current.left:
                q.append(current.left)
                next_level_num += 1
            if current.right:
                q.append(current.right)
                next_level_num += 1
            if current_level_num == 0:
                current_level_num = next_level_num
                next_level_num = 0
                res[level] = d
                d = []
                level += 1
        return res