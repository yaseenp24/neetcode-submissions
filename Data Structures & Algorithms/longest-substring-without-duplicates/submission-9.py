class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        left = 0
        most = 0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[left])
                left += 1
            current = r - left + 1
            most = max(most, current)
            charset.add(s[r])
        return most 