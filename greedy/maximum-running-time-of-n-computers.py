class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:

        sumPower = sum(batteries)
        left, right = 1, sumPower // n

        while left < right:
            target = (left + right + 1) // 2
            extra = 0

            for power in batteries:
                extra += min(power, target)

            if extra >= n * target:
                left = target
            else:
                right = target - 1

        return left


            


