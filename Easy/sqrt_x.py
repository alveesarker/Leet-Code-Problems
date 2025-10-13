class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        result = 0
        while low <= high:
            mid = (low + high)//2
            sqr = mid * mid
            if sqr <= x:
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result