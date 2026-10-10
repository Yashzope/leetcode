class Solution(object):
    def sortedSquares(self, nums):
        
        l , r = 0 , len(nums)-1
        result = [0] * len(nums)
        position = r

        while l <= r:
            if abs(nums[l]) <= abs(nums[r]):
                result[position] = nums[r] **2
                r-=1
            else:
                result[position] = nums[l] **2
                l+=1
            
            position-=1
        
        return result
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        