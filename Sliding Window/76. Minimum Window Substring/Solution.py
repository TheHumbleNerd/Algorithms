class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        resLen = float('infinity')
        map1 = {}
        for i in t:
            map1[i] = map1.get(i, 0) + 1
        
        map2 = {}
        uniqueKeys = len(map1.keys())
        matchingKeys = 0
        l, r = 0, 0
        while r < len(s):
            map2[s[r]] = map2.get(s[r], 0) + 1
            if s[r] in map1 and map2[s[r]] == map1[s[r]]:
                matchingKeys += 1
            
            while matchingKeys == uniqueKeys:
                if resLen > r - l + 1:
                    result = s[l:r+1]
                    resLen = r - l + 1
                
                if s[l] in map1 and map2[s[l]] == map1[s[l]]:
                    matchingKeys -= 1
                map2[s[l]] -= 1

                l += 1

            r += 1

        return result
