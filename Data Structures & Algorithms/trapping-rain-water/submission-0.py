class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        total = 0
        current_height = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] > current_height:
                    current_height = height[left]
                left += 1
                if (current_height - height[left]) > 0:
                    total = total + current_height - height[left] 

            elif height[left] > height[right]:
                if height[right] > current_height:
                    current_height = height[right]
                right -= 1
                if (current_height - height[right]) > 0:
                    total = total + current_height - height[right]

            
        return total