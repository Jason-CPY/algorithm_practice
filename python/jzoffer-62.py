# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        self.res = []
        self.mid(pRoot)
        return self.res[k-1] if 0<k<=len(self.res) else None
    
    def mid(self, root):
        if not root:
            return
        self.mid(root.left)
        self.res.append(root)
        self.mid(root.right)