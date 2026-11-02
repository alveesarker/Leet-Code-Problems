class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        len_nums = len(nums)
        median_index = len_nums // 2
        median = nums[median_index]
        if len_nums % 2 == 0:
            median = (nums[median_index-1] + nums[median_index]) / 2
        
        count = 0
        for i in range(len_nums):
            count += abs(nums[i] - median)

        return count
        
