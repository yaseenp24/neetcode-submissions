class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        most = 0
        while left < right:
            water = min(heights[left], heights[right]) * (right - left)
            most = max(water, most)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return most