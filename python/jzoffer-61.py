# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val) +',' + self.Serialize(root.left) +','+ self.Serialize(root.right)
    
    def Deserialize(self, s):
        # write code here
        list = s.split(',')
        return self.des(list)
    
    def des(self, list):
        if len(list)<=0:
            return None
        val = list.pop(0)
        root = None
        if val != '#':
            root = TreeNode(int(val))
            root.left = self.des(list)
            root.right = self.des(list)
        return root