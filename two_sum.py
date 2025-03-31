class Solution(object):
    def twoSum(self, nums, target):
        num_1 = 0
        num_2 = 1
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    num_1 = i
                    num_2 = j
        return [num_1, num_2]