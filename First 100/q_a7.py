"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 

That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        diction = dict()
        sortedNums = sorted(nums)
        for i in range(len(nums)):
            if sortedNums[i] not in diction:
                diction[sortedNums[i]] = i

        for i in range(len(nums)):
            nums[i] = diction[nums[i]]
        return nums
        # Time Complexity: O(nlog(n))
        # Space Complexity: O(n)
