class Solution:
    def largestHistogram(self, heights):
        stack = []
        maxArea = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                nse = i
                pse = stack[-1] if stack else -1
                maxArea = max(maxArea, height * (nse - pse - 1))
            stack.append(i)

        while stack:
            height = heights[stack.pop()]
            nse = n
            pse = stack[-1] if stack else -1
            maxArea = max(maxArea, height * (nse - pse - 1))

        return maxArea

    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        n, m = len(matrix), len(matrix[0])
        heights = [0] * m
        maxArea = 0

        for i in range(n):
            for j in range(m):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            maxArea = max(maxArea, self.largestHistogram(heights))

        return maxArea