class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        right = 0
        maxx = 0
        for i in range(len(s)):
            while right < len(s) and s[right] not in charset:
                charset.add(s[right])
                right += 1
            charset.remove(s[i])
            currmax = right - i
            maxx = max(currmax, maxx)
        return maxx