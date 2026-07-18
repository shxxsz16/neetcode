class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        stack = []
        total = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                mid = stack.pop()
                if stack:          #是if 不是while，因为找once左边有边界的话
                    left = stack[-1]
                    right = i
                    h = min(height[left],height[right]) - height[mid] #这里注意要减掉mid的高度(坑面)
                                                                      #因为是每次发现左边有更高边界的时候再升left-mid层
                    width = right - left - 1
                    total += h * width
                    
            stack.append(i)

        return total