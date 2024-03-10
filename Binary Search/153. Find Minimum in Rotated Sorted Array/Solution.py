class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        result = nums[0]
        while l <= r:

            if nums[l] <= nums[r]:
                result = min(result, nums[l])
                break

            m = l + ((r-l)//2)
            mid = nums[m]
            result = min(result, mid)
            if mid < nums[r]:
                r = m - 1
            else:
                l = m + 1
        return result
