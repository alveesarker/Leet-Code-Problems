class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        prev_col = len(grid[0])
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    count = count + ((prev_col - j) * (len(grid) - i))
                    prev_col = j
                    break
        return count
        