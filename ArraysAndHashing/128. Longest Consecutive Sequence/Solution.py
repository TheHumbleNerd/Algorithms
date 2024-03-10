class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberSet = set(nums)
        longestConsecutive = 0

        for i in nums:
            if (i - 1) not in numberSet:
                length = 1
                while (i+length) in numberSet:
                    length += 1
                longestConsecutive = max(length, longestConsecutive)

        return longestConsecutive
