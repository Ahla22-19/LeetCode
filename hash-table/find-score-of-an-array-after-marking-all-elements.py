class Solution:
    def findScore(self, nums: List[int]) -> int:

        score = 0 
        marked = [False]*len(nums)
        num_s = [(num, idx) for idx, num in enumerate(nums)]
        num_s.sort()

        for i in range(len(nums)):

            number = num_s[i][0]
            index = num_s[i][1]

            if not marked[index]:
                score += number
                marked[index] = True

                if index - 1 >= 0:
                    marked[index - 1] = True

                if index + 1 < len(nums):
                    marked[index + 1] = True

        return score



