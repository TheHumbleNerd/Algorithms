class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        result = []

        for word in strs:
            hash = ''.join(sorted(word))
            if hash in hashmap:
                hashmap[hash].append(word)
            else:
                hashmap[hash] = [word]
        
        for i, (key, value) in enumerate(hashmap.items()):
            result.append(value)
        
        return result
    