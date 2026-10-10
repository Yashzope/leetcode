class Solution(object):
    def reverseStr(self, s, k):
        char = list(s)
        n = len(s)

        for start in range(0,n,2*k):
            l , r = start , min(start + k-1,n-1)
        
            while l < r:
                char[l] , char [r] = char[r] , char [l]
                l+=1
                r-=1
        
        return "".join(char)
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        