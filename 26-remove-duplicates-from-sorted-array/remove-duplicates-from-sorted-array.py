class Solution(object):
    def removeDuplicates(self, nums):
        s = 1
        for f in range(1,len(nums)):
            if nums[f] != nums[s-1]:  
                nums[s] , nums[f] = nums[f] ,nums[s]
                s+=1
        return s    