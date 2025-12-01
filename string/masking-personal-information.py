class Solution:
    def maskPII(self, s: str) -> str:
        ans = ''
        ans += s[0].lower()
        ans += 5 * "*"

        if s[0].isalpha():

            for i in range (1,len(s)):
                if i + 1 < len(s) and not s[i + 1] == "@":
                    continue
                else:
                    ans += s[i].lower()
                    break
            ans += s[i+1:].lower()
            
            return ans

        else:
            res = ''
            num_ans = ''
            for i in range(len(s)):
                if s[i].isdigit():
                    res += s[i]

            l = len(res)

            if l == 13:
                num_ans += "+***-***-***-"

            elif l == 12:
                num_ans += "+**-***-***-"

            elif l == 11:
                num_ans += "+*-***-***-"
            
            else:
                num_ans += "***-***-"

            num_ans += res[-4:]
            return num_ans
