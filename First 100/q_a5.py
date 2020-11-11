"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""


class Solution(object):
    def shuffle(self, nums, n):
        if len(nums) != 2*n:
            return None
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
