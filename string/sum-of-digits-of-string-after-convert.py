class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        ans = ''
        for i in range(len(s)):
            a = ord(s[i]) - ord("a") + 1
            ans += str(a)

        for i in range(k):
            list_ans = [int(num) for num in ans]
            s  = sum(list_ans)
            ans = str(s)
        
        return s

            

            