class Solution(object):
    def mergeAlternately(self, word1, word2):
        i , j = 0 , 0 
        result = ""

        while i < len(word1) and j < len(word2):
            result+=word1[i] 
            result+=word2[j] 
            i+=1
            j+=1
        while i < len(word1):
            result+=word1[i]
            i+=1

        while j < len(word2):
            result+=word2[j]
            j+=1 
        return result
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        