class Solution(object):
    def twoSum(self, nums, target):
        ind=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    ind.extend([i,j])
                    break
        return ind

        