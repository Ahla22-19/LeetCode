class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        CountNums = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]

        for num, count in CountNums.items():
            freq[count].append(num)

        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)

            if len(ans) == k:
                return ans


            
            