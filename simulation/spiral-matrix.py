class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows, columns = len(matrix), len(matrix[0])
        top, bottom, left, right = 0 ,rows, 0, columns
        spiral = [] 

        while left < right and top < bottom:

            #from left to right
            for i in range(left, right):
                spiral.append(matrix[left][i])
            top += 1

            #from top to bottom
            for i in range(top, bottom):
                spiral.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            #from right to left
            for i in range(right - 1, left - 1, -1):
                spiral.append(matrix[bottom - 1][i])
            bottom -= 1

            #from bottom to top
            for i in range(bottom - 1, top - 1, -1):
                spiral.append(matrix[i][left])
            left += 1

        return spiral





















            
