class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        row, column = len(matrix), len(matrix[0])
        ans = [[0]*row for i in range(column)]
        
        for r in range(row):
            for c in range (column):
                ans[c][r] = matrix[r][c]
        
        return ans


