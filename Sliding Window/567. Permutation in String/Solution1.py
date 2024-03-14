class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        map1 = {}
        for i in s1:
            map1[i] = map1.get(i, 0) + 1
        windowSize = len(s1)

        map2 = {}
        l, r = 0, 0
        while r < windowSize:
            map2[s2[r]] = map2.get(s2[r], 0) + 1
            r += 1
        if map1 == map2:
            return True
        while r < len(s2):
            map2[s2[l]] -= 1
            if map2[s2[l]] == 0:
                map2.pop(s2[l])
            map2[s2[r]] = map2.get(s2[r], 0) + 1
            l += 1
            r += 1
            if map1 == map2:
                return True
        return False
