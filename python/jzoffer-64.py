# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not size or size>len(num):
            return []
        cur_max = max(num[:size])
        max_nums = [cur_max]
        for i in range(0, len(num) - size):
            if num[i] == cur_max:
                cur_max = max(num[i + 1:i + size + 1])
            elif num[i + size] > cur_max:
                cur_max = num[i + size]
            max_nums.append(cur_max)
        return max_nums