class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        
        current_l, current_r = 1, 1

        for i in range(len(nums)):
            left [i] = current_l
            current_l *= nums[i]

        for j in  range(len(nums)-1, -1, -1):
            right[j] = current_r
            current_r *= nums[j]
            
        expect = [1] * len(nums)

        for q in range(len(nums)):
            expect[q] = left[q] * right [q]

        return expect