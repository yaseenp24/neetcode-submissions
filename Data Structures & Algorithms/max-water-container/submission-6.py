class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        largest = 0
        while left < right:
            if heights[left] < heights[right]:
                total = heights[left] * (right - left)
                left += 1
            else:
                total = heights[right] * (right - left)
                right -= 1
            largest = max(total, largest)

        return largest