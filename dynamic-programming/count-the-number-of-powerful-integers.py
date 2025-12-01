class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def solve(s: str, input_suffix: str, limit: int) -> int:
            if len(s) < len(input_suffix):
                return 0

            count = 0
            trail_string = s[-len(input_suffix):]  
            remain_l = len(s) - len(input_suffix)

            for i in range(remain_l):
                digit = int(s[i])
                if digit <= limit:
                    count += digit * pow(limit + 1, remain_l - i - 1)
                else:
                    count += pow(limit + 1, remain_l - i)
                    return count  

            if trail_string >= input_suffix:
                count += 1

            return count

        start_str = str(start - 1)
        finish_str = str(finish)
        
        return solve(finish_str, s, limit) - solve(start_str, s, limit)

        