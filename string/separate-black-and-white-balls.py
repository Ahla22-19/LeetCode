class Solution:
    def minimumSteps(self, s: str) -> int:

        left = 0
        right = len(s) - 1        
        swap_count = 0

        while left < right:

            if s[left] == "1" and s[right] == "0":
                swap_count += right - left
                left += 1
                right -= 1

            elif s[left] == "0":
                left += 1
            
            else:
                right -= 1
            

        return swap_count

        