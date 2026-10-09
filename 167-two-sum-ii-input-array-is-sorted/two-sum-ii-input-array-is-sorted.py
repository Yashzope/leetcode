class Solution(object):
    def twoSum(self, numbers, target):
        l = 0 
        r = len(numbers) - 1
        
        while l < r:
            total = numbers[l] + numbers[r]
            if target == total:
                return [l+1 ,r+1]
            else:
                if target < numbers[l] + numbers[r]:
                    r-=1
                else:
                    l+=1
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        