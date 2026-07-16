class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_water = 0

        while left < right:
            height = min(heights[left],heights[right])
            width = right - left
            max_water = max(max_water,height * width)
            print(height, width,height * width)

            if height == heights[left] and left < right:
                left += 1

            elif left < right:
                right -= 1

        return max_water