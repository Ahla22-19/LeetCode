class Solution:
    def kthCharacter(self, k: int) -> str:

        def generate(S):

            if len(S) >= k:
                return S[k - 1]
            next_ = S

            for i in range(len(S)):
                if S[i] == 'z':
                    next_ += 'a'
                else:
                    next_ += (chr(ord(S[i]) + 1)) 

            return generate(next_)

        S = 'a'
        ans = generate(S)
        return ans