class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)

        if max(nums2) < 0 and min(nums1) > 0:
            return max(nums2) * min(nums1)

        prev = [0] * (len(nums2) + 1)

        for i in range(len(nums1)-1, -1, -1):
            dp = [0] * (len(nums2) + 1)
            for j in range(len(nums2)-1, -1, -1):
                use = nums1[i] * nums2[j] + prev[j+1]
                dp[j] = max(use, prev[j], dp[j+1])
            prev = dp
        return dp[0]
        