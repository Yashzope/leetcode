class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
    """
        l = 0
        r = len(nums)-1
        

        while l < r:
            if nums[l] + nums[r] == target:
                return[l,r]
            elif nums[l] + nums[r] > target:
                r-=1
            else:
                l+=1
        return []      

       
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        