class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        left = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[r])
            length = r - left + 1
            longest = max(longest, length)
        return longest
