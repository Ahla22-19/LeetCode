class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                check1 = s[left + 1:right + 1]
                check2 = s[left:right]

                return (check1 == check1[::-1]
                       or check2 == check2[::-1])
            left += 1
            right -= 1


        return True