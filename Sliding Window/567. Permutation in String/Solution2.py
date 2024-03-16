class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        map1 = {}
        for i in s1:
            map1[i] = map1.get(i, 0) + 1
        windowSize = len(s1)
        uniqueKeys = len(map1.keys())
        matchingKeys = 0
        map2 = {}

        l, r = 0, 0
        while r < windowSize:
            map2[s2[r]] = map2.get(s2[r], 0) + 1
            r += 1
        for key in map2.keys():
            if map2[key] == map1.get(key, 0):
                matchingKeys += 1

        if matchingKeys == uniqueKeys:
            return True

        while r < len(s2):
            if map2[s2[l]] == map1.get(s2[l], -1):
                    matchingKeys -= 1
            map2[s2[l]] -= 1
            if map2[s2[l]] == map1.get(s2[l], -1):
                matchingKeys += 1
            l += 1

            matchingBefore = map2.get(s2[r], 0) == map1.get(s2[r], -1)
            map2[s2[r]] = map2.get(s2[r], 0) + 1
            if map2[s2[r]] == map1.get(s2[r], -1):
                    matchingKeys += 1
            elif matchingBefore and map2[s2[r]] > map1.get(s2[r], 0):
                matchingKeys -= 1
            
            r += 1
            if matchingKeys == uniqueKeys:
                return True
        return False
