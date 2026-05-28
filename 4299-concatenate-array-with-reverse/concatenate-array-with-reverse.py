class Solution(object):
    def concatWithReverse(self, nums):
        B = []
        for i in nums:
            B.append(i)
        B.extend(nums[::-1])
        return B