class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        deq = collections.deque()
        for i in range(k):
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)
        
        result.append(nums[deq[0]])
        for i in range(k, len(nums), 1):
            if deq[0] < i-k+1:
                deq.popleft()

            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)
            
            result.append(nums[deq[0]])
        
        return result
