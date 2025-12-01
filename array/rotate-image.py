class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        right,left = len(matrix) - 1, 0

        while left < right:
            for i in range(right - left):

                top, bottom = left, right

                # save the top left value
                topLeft = matrix[top][left + i]

                # from bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # from bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # from top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                #from top left to top right
                matrix[top + i][right] = topLeft

            right -=1
            left += 1

                 
        