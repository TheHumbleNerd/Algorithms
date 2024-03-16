class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        map1 = {}
        for i in t:
            map1[i] = map1.get(i, 0) + 1
        
        map2 = {}
        uniqueKeys = len(map1.keys())
        matchingKeys = 0
        l, r = 0, 0
        while r < len(s):
            while r < len(s) and matchingKeys != uniqueKeys:
                map2[s[r]] = map2.get(s[r], 0) + 1
                if map2[s[r]] == map1.get(s[r], -1):
                    matchingKeys += 1
                r += 1
            
            while l < r and l < len(s) and matchingKeys == uniqueKeys:
                tempResult = s[l:r]
                if len(result) == 0 or len(tempResult) < len(result):
                    result = tempResult
                
                if map2[s[l]] == map1.get(s[l], -1):
                    matchingKeys -= 1
                map2[s[l]] -= 1

                l += 1
            
        return result
