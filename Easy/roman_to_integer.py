class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 
            'C': 100, 'D': 500, 'M': 1000
        }
        int_num = 0
        prev = 0
        for i in s:
            val = roman_map[i]
            if val > prev:
                int_num += (val - 2*prev)
            else:
                int_num += val
            prev = val
        
        return int_num