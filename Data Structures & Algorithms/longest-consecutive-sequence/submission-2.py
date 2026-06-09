class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        array = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in array:
                length = 1
                while (num + 1) in array:
                    length += 1
                    num = num + 1
                longest = max(longest, length)
        return longest