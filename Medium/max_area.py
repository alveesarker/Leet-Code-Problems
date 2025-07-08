class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_point = 0
        right_point = -1
        max_area = 0
        height_len = len(height)
        while abs(right_point) + left_point != height_len:
            tow_point_area = (height_len + right_point - left_point) * min(height[left_point], height[right_point])
            if max_area < tow_point_area:
                max_area = tow_point_area
            if height[left_point] < height[right_point]:
                left_point += 1
            elif height[left_point] > height[right_point]:
                right_point -= 1
            else:
                left_point += 1
        return max_area
        