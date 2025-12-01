class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:

        stack = []
        ans = [0] * len(t)
        
        for idx, temp in enumerate(t):

            while stack and temp > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                ans[stackIdx] = (idx - stackIdx)
                
            stack.append([temp, idx])

        return ans



                
