class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxW = 0 
        l = 0
        r = len(heights)-1

        while l < r:
            if heights[l] < heights[r]:
                area = heights[l] * (r-l)
                l+=1
            else:
                area = heights[r] * (r-l)
                r-=1
            maxW = max(maxW, area)

        return maxW