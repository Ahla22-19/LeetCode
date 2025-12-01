class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        count_0 = 0
        count_1 = 0
        ans = ""

        for num in s:

            if num == '1':
                count_1 += 1
            else:
                count_0 += 1

        for i in range(count_1 - 1):
            ans += '1'

        for i in range(count_0):
            ans += '0'

        return ans + '1'

        