class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        count_pro = defaultdict(int)
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[j] * nums[i]
                count += count_pro[product]
                count_pro[product] += 1

        return count * 8

                
        



