class Solution:
    def maximumLength(self, s: str) -> int:

        count_str = {}

        for i in range (len(s)):
            cur_string = ""

            for j in range(i, len(s)):

                if not cur_string or cur_string[-1] == s[j]:
                    cur_string += s[j]

                    if cur_string in count_str:
                        count_str[cur_string] += 1
                    else:
                        count_str[cur_string] = 1

                else:
                    break 

        ans = 0  
        for item, freq in count_str.items():
            if len(item) > ans and freq >= 3:
                ans = len(item)
        
        if ans > 0: return ans
        return -1
        
                
