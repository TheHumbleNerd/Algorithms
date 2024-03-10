class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        map1 = {}
        for i in s:
            map1[i] = map1.get(i, 0) + 1

        for i in t:
            map1[i] = map1.get(i, 0) - 1

        for key in map1:
            if map1[key] != 0:
                return False

        return True
