class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total = 0
        neg_count = 0
        smallest_abs = float('inf')
        zero_exist = False
        for i in matrix:
            for j in i:
                val = abs(j)
                if j < 0:
                    neg_count+=1
                if val < smallest_abs:
                    smallest_abs = val
                
                if j == 0:
                    zero_exist = True
                total += val
        
        if zero_exist or neg_count % 2 == 0:
            return total
        else:
            return total - (2 * smallest_abs)

