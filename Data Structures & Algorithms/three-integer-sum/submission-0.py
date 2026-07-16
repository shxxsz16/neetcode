class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        print(nums)

        three_sum =[]
        fix = 0

        while fix < len(nums)-2:
            if fix>0 and nums[fix] == nums[fix-1]:
                fix += 1
                continue

            target = 0 - nums[fix]
            left = fix+1
            right = len(nums)-1

            while left < right:
                if nums[left]+nums[right] < target :
                    left += 1
                elif nums[left]+nums[right] > target :
                    right -= 1
                elif nums[left]+nums[right] == target:
                    three_sum.append([nums[fix],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left<right and nums[left] == nums[left-1]:
                        left += 1

                    while left<right and nums[right] == nums[right+1]:
                        right -= 1
            
            fix += 1

        return three_sum
