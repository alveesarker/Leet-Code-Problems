class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matched_bracket = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                last_o_b = stack[-1]
                if matched_bracket[last_o_b] == i:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False