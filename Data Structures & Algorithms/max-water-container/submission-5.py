class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        largest = 0
        while left < right:
            total = min(heights[left], heights[right]) * (right - left)
            largest = max(total, largest)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return largest