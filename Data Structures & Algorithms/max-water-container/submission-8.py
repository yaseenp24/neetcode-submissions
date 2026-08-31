class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        res = 0
        while left < right:
            total = min(heights[left], heights[right]) * (right - left)
            res = max(res, total)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return res