class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_s = set()
        l = 0
        max_length = 0

        for i in range(len(s)):
            while s[i] in char_s:
                char_s.remove(s[l])
                l += 1
            char_s.add(s[i])
            max_length = max(max_length, i - l + 1)
        return max_length