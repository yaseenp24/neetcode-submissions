class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashh = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashh:
                return [hashh[diff], i]
            hashh[nums[i]] = i
        
