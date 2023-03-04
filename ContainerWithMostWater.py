class Solution:
    def max_area(self, height):
        left, right, area = 0, len(height) - 1, 0
        while left < right:
            area = max(area, (right - left)*min(height[right], height[left]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1