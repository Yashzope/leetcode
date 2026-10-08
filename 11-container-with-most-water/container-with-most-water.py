class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        maxx = 0

        while l < r:
            """length = min(height[l],height[r])
            width = r - l 
            """
            area = min(height[l],height[r]) * (r-l)
            if area > maxx: 
                maxx = area
                
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxx        
        """
        :type height: List[int]
        :rtype: int
        """
        