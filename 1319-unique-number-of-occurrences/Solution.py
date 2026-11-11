class Solution(object):
    def uniqueOccurrences(self, arr):
        d = {}
        for i in range(len(arr)):
            d[arr[i]] = d.get(arr[i],0) +1
        return len(d.values()) == len(set(d.values()))