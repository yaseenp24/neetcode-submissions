class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            multiply = 1
            for j in range(len(nums)):
                if j != i:
                    multiply = multiply * nums[j]
            output.append(multiply)
        return output