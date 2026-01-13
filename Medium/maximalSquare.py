class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def largestSquareArea(heights):
            n = len(heights)

            right = [0] * n
            stack = []
            for i in range(n - 1, -1, -1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                right[i] = stack[-1] if stack else n
                stack.append(i)

            left = [0] * n
            stack = []
            for i in range(n):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                left[i] = stack[-1] if stack else -1
                stack.append(i)

            max_area = 0
            for i in range(n):
                width = right[i] - left[i] - 1
                if width >= heights[i]:
                    max_area = max(max_area, heights[i] * heights[i])

            return max_area

        n = len(matrix[0])
        row_n = len(matrix)
        row = [0] * n
        m_a = 0
        
        for k in range(row_n):
            for l in range(n):
                if int(matrix[k][l]) == 0:
                    row[l] = 0
                else:
                    row[l] = row[l] + int(matrix[k][l])
            a = largestSquareArea(row)
            m_a = max(a, m_a)
        return m_a
        
        
        
