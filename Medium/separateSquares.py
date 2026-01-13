class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        mx_y = float('-inf')
        mn_y = float('inf')
        total_area = 0
        for i in squares:
            mx_y = max(i[1] + i[2], mx_y)
            mn_y = min(i[1], mn_y)
            total_area += (i[2]*i[2])

        half_area = total_area / 2.0
        while mx_y - mn_y > 1e-6:
            mid = (mn_y + mx_y) / 2.0
            curr_total_area = 0
            for x, y, s in squares:
                if y < mid:
                    height = min(s, mid - y)
                    curr_total_area += s * height

            if curr_total_area >= half_area:
                mx_y = mid
            else:
                mn_y = mid
        return round(mx_y, 5)