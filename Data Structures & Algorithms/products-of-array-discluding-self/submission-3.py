class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n  # Initialize output array with 1s
        
        # Step 1: Calculate left products for each element
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]
        
        # Step 2: Calculate right products and multiply them with the left products
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        
        return output