class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        ans = 0
        count = defaultdict(int)
        distinct = len(set(nums))
        
        right = 0
        for left in range(len(nums)):

            if left > 0:
                remove = nums[left - 1]
                count[remove] -= 1
                if count[remove] == 0:
                    count.pop(remove)

            while right < len(nums) and len(count) < distinct:
                element = nums[right] 
                count[element] += 1
                right += 1

            if len(count) == distinct:
                ans += len(nums) - right + 1

        return ans




        
        