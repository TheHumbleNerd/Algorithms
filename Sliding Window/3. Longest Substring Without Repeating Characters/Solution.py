class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStrSet = set()
        l, r = 0, 0
        maxLength = min(1, len(s))
        while r < len(s):
            if s[r] in subStrSet:
                maxLength = max(maxLength, len(subStrSet))
                while l < r and s[r] in subStrSet:
                    subStrSet.remove(s[l])
                    l += 1
            subStrSet.add(s[r])
            r += 1
        maxLength = max(maxLength, len(subStrSet))
        return maxLength
