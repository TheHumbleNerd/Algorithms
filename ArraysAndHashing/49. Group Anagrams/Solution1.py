class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        result = []

        for word in strs:
            found = False
            for key in hashmap:
                if self.isAnagram(word, key):
                    hashmap[key].append(word)
                    found = True
                    break
            if not found:
                hashmap[word] = [word]
        
        for i, (key, value) in enumerate(hashmap.items()):
            result.append(value)
        
        return result

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map1, map2 = {}, {}
        for i in s:
            map1[i] = map1.get(i, 0) + 1
        for i in t:
            map2[i] = map2.get(i, 0) + 1

        return map1 == map2
    