class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            m = (left + right) // 2
            if target == nums[m]:
                return m
            if nums[left] <= nums[m]:
                if nums[left] > target or target > nums[m]:
                    left = m + 1
                else:
                    right = m - 1 
            else:
                if nums[m] > target or target > nums[right]:
                    right = m - 1
                else:
                    left = m + 1
        return -1
