class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        l = 0
        finalCount = 0
        for r in range(len(s)):
            while s[r] in letters:
                letters.discard(s[l])
                l += 1
            letters.add(s[r])
            finalCount = max(finalCount, r - l + 1)
        return finalCount
