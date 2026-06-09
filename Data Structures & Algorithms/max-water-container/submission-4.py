class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        left, right = 0, len(heights)-1
        while left < right:
            currmax = 0
            if heights[left] <= heights[right]: 
                currmax = heights[left] * (right - left)
                left += 1
            elif heights[left] > heights[right]:
                currmax = heights[right] * (right - left)
                right -= 1
            maximum = max(maximum, currmax)
        return maximum 