# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return []
        B = [1]*len(A)
        for i in range(len(A)):
            C = A[:]
            C.pop(i)
            for j in range(len(C)):
                B[i] *= C[j]
        return B