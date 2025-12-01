class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        num = int(sqrt(c))

        i = 0
        while i <= num:
            ans = pow(i, 2) + pow(num, 2)

            if ans == c:
                return True

            elif ans < c:
                i += 1

            else:
                num -= 1

        return False

        