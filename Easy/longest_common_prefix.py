class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        if len(min(strs)) == 0:
            return ""
        pref = ""
        for i in range(len(min(strs))):
            if strs[0] == "":
                return ""
            else:
                pref_zero = strs[0][i]
            for j in strs:
                if j == "":
                    return ""
                else:
                    if j[i] != pref_zero:
                        return pref
            pref += strs[0][i]
        return pref