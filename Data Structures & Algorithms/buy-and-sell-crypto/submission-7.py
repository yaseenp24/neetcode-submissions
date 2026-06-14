class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        largest = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                largest = max(largest, profit)
            else:
                left = right
            right += 1
        return largest