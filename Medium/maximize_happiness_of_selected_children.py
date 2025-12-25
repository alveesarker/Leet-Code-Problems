class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort()
        len_h = len(happiness)
        sum_h = 0
        for i in range(k):
            val = happiness[len_h -i -1] - i
            if val <= 0:
                break
            sum_h += val
        return sum_h

        