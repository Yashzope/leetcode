class Solution(object):
    def moveZeroes(self, nums):
        s = 0
        for f in range(len(nums)):
            if nums[f] != 0:
                nums[s] , nums[f] = nums[f] , nums[s]
                s+=1
        return nums