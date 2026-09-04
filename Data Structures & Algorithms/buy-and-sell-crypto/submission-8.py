class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxp = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                current = prices[right] - prices[left]
                maxp = max(maxp, current)
            else:
                left = right
            right += 1

        return maxp
        
        # while right < len(prices)-1:
        #     while prices[right] > prices[left] and right < len(prices)-1:
        #         right += 1
        #     current = prices[right] - prices[left]
        #     maxp = max(maxp, current)
        #     left = right
        #     right += 1
        # return maxp