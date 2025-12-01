class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        prefix = [0] * (len(s) + 1)

        for start, end, d in shifts:
            prefix[end + 1] += 1 if d else -1
            prefix[start] += -1 if d else 1
    
        res = [ord(char) - ord("a") for char in s]
        diff = 0

        for i in reversed(range(len(prefix))):
            diff += prefix[i]
            res[i - 1] = (diff + res[i -1]) % 26

        s = [chr(ord("a") + num) for num in res]

        return "".join(s)