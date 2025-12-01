class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        rows, columns = len(matrix), len(matrix[0])
        self.pre_mat = [[0] * (columns + 1)  for r in range(rows + 1)]

        for r in range(rows):
            prefix = 0
            for c in range(columns):
                prefix += matrix[r][c]
                above = self.pre_mat[r][c + 1]
                self.pre_mat[r + 1][c + 1] = prefix + above
       
        
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:

        r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1

        bottom_right = self.pre_mat[r2][c2] 
        above = self.pre_mat[r1 - 1][c2]
        left = self.pre_mat[r2][c1 - 1]
        top_left = self.pre_mat[r1 - 1][c1 - 1]

        return bottom_right - above - left  + top_left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)