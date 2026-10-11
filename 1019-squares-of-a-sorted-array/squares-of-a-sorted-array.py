class Solution(object):
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i] *= nums[i]
        a = sorted(nums)
        return a