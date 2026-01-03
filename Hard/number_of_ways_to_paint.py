class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        same = 6
        diff = 6

        for _ in range(2, n + 1):
            new_diff = (diff * 2 + same * 2) % MOD
            new_same = (diff * 2 + same * 3) % MOD

            diff = new_diff
            same = new_same

        return (same + diff) % MOD
        