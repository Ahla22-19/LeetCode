class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        rows, columns = len(matrix), len(matrix[0])
        for j in range (rows):
            for i in range(columns):
                if j < rows - 1 and i < columns - 1:
                    if matrix[j][i] != matrix[j+1][i+1]:
                        return False
        return True
        
                    