class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        result = []
        nums.sort()

        while i < len(nums)-2:
            if i > 0 and nums[i-1] == nums[i]:
                i += 1
                continue

            target = -nums[i]
            j, k = i+1, len(nums)-1
            while j < k:
                sum = nums[j] + nums[k]
                if sum == target:
                    result.append([nums[i],nums[j],nums[k]])
                    while (j < len(nums)-1 and nums[j+1] == nums[j]):
                        j += 1
                    j += 1
                elif sum > target:
                    k -= 1
                else:
                    j += 1
            i += 1

        return result
