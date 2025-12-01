class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = ""

        for i in range (len(s)):
            if s[i].isalpha() or s[i].isdigit():
                new_s += s[i].lower()

        if new_s == new_s[::-1]:
            return True

        return False 