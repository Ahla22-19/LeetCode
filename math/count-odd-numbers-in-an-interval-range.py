class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            if (i + 1) % 2 == 0:
                count += 1

        return count
