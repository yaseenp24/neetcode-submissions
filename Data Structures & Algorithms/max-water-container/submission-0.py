class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        for i in range(len(heights)-1):
            right = i + 1
            while right < len(heights):
                area = ((right - i) * min(heights[i], heights[right]))
                if area > maxarea:
                    maxarea = area
                right += 1
        return maxarea