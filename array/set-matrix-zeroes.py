class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, columns = len(matrix), len(matrix[0])
        index_zeros = []

        for j in range (rows):
            for i in range(columns):
                if matrix[j][i] == 0:
                    index_zeros.append([j, i])
        
        for k in range(len(index_zeros)):
            for l in range(rows):
                matrix[l][index_zeros[k][1]] = 0

            for l in range(columns):
                matrix[index_zeros[k][0]][l] = 0

        return matrix




                    