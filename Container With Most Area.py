# 从两头开始找起，因为这保证了宽是递减的，在接下来的查找中，要想area变大，则必须长变大，这保证了只需关注“长”这一单变量，时间复杂度为O(n)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            current_area = current_height * width

            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return max_area
