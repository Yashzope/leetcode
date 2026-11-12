class Solution(object):
    def runningSum(self, nums):
        lst = []
        count = 0
        for i in nums:
            count+= i
            a = count
            lst.append(a)
        return lst