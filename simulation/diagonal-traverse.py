class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        diagonals = defaultdict(list)
        rows, columns = len(mat), len(mat[0])

        for r in range(rows):
            for c in range(columns):
                diagonals[r + c].append(mat[r][c])

        ans = []
        for key, value in diagonals.items():

            if key % 2 == 0:
                ans.extend(reversed(value))

            else:
                ans.extend(value)

        return ans






