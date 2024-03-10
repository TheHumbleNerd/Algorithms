class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        frequency = [[] for i in range(len(nums)+1)]

        for key, val in hashmap.items():
            frequency[val].append(key)
        
        res = []
        for i in range(len(frequency)-1, -1, -1):
            for j in frequency[i]:
                res.append(j)
                if len(res) == k:
                    break
            if len(res) == k:
                break

        return res
