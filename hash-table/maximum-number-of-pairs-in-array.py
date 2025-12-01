class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:

        count = Counter(nums)
        ans = [0, 0]

        for key ,value in count.items():
            if count[key] % 2 == 1:
                ans[1] += 1
            ans[0] += count[key] // 2
        return ans

            
        