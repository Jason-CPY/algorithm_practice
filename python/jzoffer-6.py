# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # if not rotateArray:
        #     return 0
        # if len(rotateArray) == 1:
        #     return rotateArray[0]
        # if len(rotateArray) == 2:
        #     if rotateArray[0] >= rotateArray[1]:
        #         return rotateArray[1]
        #     else:
        #         return rotateArray[0]
        # l = len(rotateArray)
        # if rotateArray[l/2] > rotateArray[0]:
        #     return self.minNumberInRotateArray(rotateArray[l/2:])
        # elif rotateArray[l/2] <= rotateArray[0]:
        #     return self.minNumberInRotateArray(rotateArray[:l/2+1])
        if not rotateArray:
            return 0
        if len(rotateArray) == 1:
            return rotateArray[0]
        l = len(rotateArray)
        left = 0
        right = l-1
        while left <= right:
            mid = (left+right)/2
            if rotateArray[mid] > rotateArray[right]:
                left = mid+ 1
            elif rotateArray[mid] < rotateArray[right]:
                right = mid
            else:
                right -= 1
            if left >= right:
                break
        return rotateArray[left]


if __name__ == '__main__':
    s = Solution()
    a = [6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]
    print s.minNumberInRotateArray(a)