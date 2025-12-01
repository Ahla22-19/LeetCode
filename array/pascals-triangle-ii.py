class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]

        prev_row = self.getRow(rowIndex - 1)
        ans = [1]

        for i in range(len(prev_row) - 1):
            ans.append(prev_row[i] + prev_row[i + 1])
        ans.append(1)

        return ans

