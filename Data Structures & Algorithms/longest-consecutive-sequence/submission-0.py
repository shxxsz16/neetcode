class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for i in range(len(nums)):
            if nums[i]-1 not in nums_set:
                current = nums[i]
                length = 1
                
                while current + 1 in nums_set:
                    length += 1
                    current += 1

                longest = max (longest, length)

        return longest