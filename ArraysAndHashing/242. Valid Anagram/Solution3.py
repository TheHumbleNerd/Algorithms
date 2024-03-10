class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map1, map2 = {}, {}
        for i in s:
            map1[i] = map1.get(i, 0) + 1
        for i in t:
            map2[i] = map2.get(i, 0) + 1

        # for i in s:
        #     if map1[i] != map2.get(i, 0):
        #         return False

        # return True

        return map1 == map2
