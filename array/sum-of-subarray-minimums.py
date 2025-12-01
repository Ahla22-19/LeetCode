class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        arr = [-math.inf] + arr + [-math.inf]
        stack = []
        res = 0

        for idx in range(len(arr)):

            while stack and arr[stack[-1]] > arr[idx]:
                poped_idx = stack.pop()

                left = stack[-1]
                right = idx

                res += arr[poped_idx] * (poped_idx - left) * (right - poped_idx)

            stack.append(idx)
    
        return res % (10**9 + 7)
        
        