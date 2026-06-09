class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right, maxp = 0, 1, 0
        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxp = max(maxp, profit)
            else:
                left = right
            right += 1
        return maxp