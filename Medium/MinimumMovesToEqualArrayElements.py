# General Version
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        len_nums = len(nums)
        moves = 0
        for i in range(len_nums - 1):
            moves += (nums[i+1] - nums[i]) * (len_nums - i - 1)

        return moves
  
# Optimized Version  
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_v = min(nums)
        return (sum(nums) - min_v) - ((len(nums) - 1) * min_v)
        