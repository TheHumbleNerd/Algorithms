class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        l = 0
        longestSubstrLength = 0
        for r in range(len(s)):
            hashMap[s[r]] = hashMap.get(s[r], 0) + 1
            maxFreq = max(hashMap.values())
            if (r - l + 1) - maxFreq > k:
                hashMap[s[l]] -= 1
                l += 1
            longestSubstrLength = max(longestSubstrLength, r-l+1)
        
        return longestSubstrLength
