class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
            
        else:
            x = str(x)
            palindrome = x[::-1] 

            if x == palindrome:
                return True
            else:
                return False
        
        