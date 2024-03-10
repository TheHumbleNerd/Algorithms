class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        result = []

        for word in strs:
            hashableList = [0]*26
            for c in word:
                hashableList[ord(c) - ord('a')] += 1
            
            hash = tuple(hashableList)
            if hash in hashmap:
                hashmap[hash].append(word)
            else:
                hashmap[hash] = [word]
        
        for i, (key, value) in enumerate(hashmap.items()):
            result.append(value)
        
        return result
    