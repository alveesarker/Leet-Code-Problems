class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        p = x
        if x < 0:
            return False
        rev_x = 0
        while x > 0:
            last_dig = x % 10
            x //= 10
            rev_x = (rev_x * 10) + last_dig
        if rev_x == p:
            return True
        else:
            return False