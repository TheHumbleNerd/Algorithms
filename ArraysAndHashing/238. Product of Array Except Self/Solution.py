class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in range(0, len(nums))]

        prefix = 1
        for i in range(1, len(nums), 1):
            prefix = prefix*nums[i-1]
            res[i] = prefix
        
        suffix = 1
        for i in range(len(nums)-2, -1, -1):
            suffix = suffix*nums[i+1]
            res[i] = res[i]*suffix

        return res
    