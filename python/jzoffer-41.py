# -*- coding:utf-8 -*-
import math
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        ans = []
        l = []
        n = int(math.sqrt(2*tsum))
        j = 0
        k = tsum/n - (n-1)/2
        while n >= 2:
            if (n & 1) == 1 and tsum % n == 0 or (tsum % n) * 2 == n:
                while j < n:
                    l.append(k)
                    j += 1
                    k += 1
                ans += l
            n -= 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print s.FindContinuousSequence(3)