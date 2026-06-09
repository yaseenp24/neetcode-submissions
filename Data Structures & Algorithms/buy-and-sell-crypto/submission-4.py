class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        largest = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                largest = max(largest, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return largest
        #     while prices[right] < prices[left] and right < len(prices) - 1:
        #         right += 1
        #     total = prices[right] - prices[left]
        #     largest = max(largest, total)
        #     left += 1
        # return largest