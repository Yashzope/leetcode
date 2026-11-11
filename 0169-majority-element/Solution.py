class Solution(object):
    def majorityElement(self, nums):
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i],0) +1
        max_k ,max_v = 0 , float("-inf")
        for k,v in d.items():
            if v > max_v:
                max_v = v
                max_k = k
        return max_k