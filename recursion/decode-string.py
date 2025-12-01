class Solution:
    def decodeString(self, s: str) -> str:

        def decode(pointer):
            ans = []
            num = ""

            while pointer < len(s):

                if s[pointer].isdigit():
                    num+=s[pointer]
                    pointer+=1

                elif s[pointer] == "[":
                    decoded , pointer = decode(pointer+1)
                    pointer+=1
                    ans.append (int(num)*decoded)
                    num = ""

                elif s[pointer] == "]":
                    return "".join(ans) , pointer
                    
                else:
                    ans.append(s[pointer])
                    pointer+=1

            return "".join(ans)

        return decode(0)


