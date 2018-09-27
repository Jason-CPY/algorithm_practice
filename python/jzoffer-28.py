# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        dic = {}
        l = 0
        for i in numbers:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            l += 1
        for j in dic:
            if dic[j] > l/2:
                return j
        return 0

if __name__ == '__main__':
    s = Solution()
    a = [1,2,3,2,2,2,5,4,2]
    print s.MoreThanHalfNum_Solution(a)