class Solution:
    def isValidSpeed(self, k, piles: List[int], h):
        t = 0
        for i in piles:
            t += math.ceil(i/k)
        return t <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r
        while l <= r:
            m = l + ((r-l)//2)
            if self.isValidSpeed(m, piles, h):
                result = min(result, m)
                r = m - 1
            else:
                l = m + 1
        return result
