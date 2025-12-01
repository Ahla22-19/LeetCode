class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def check(counter_t, counter_s):
            for key,value in counter_t.items():
                
                if counter_s[key] < value:
                    return False

            return True

        counter_t = Counter(t)
        counter_s = Counter()

        left = 0
        min_window = float("inf")
        index = []

        for right in range(len(s)):
            counter_s[s[right]] += 1

            while check(counter_t, counter_s): 
                #all the fuction can be just replaced by counter_t <= counter_s

                if min_window > right - left + 1:
                    index = [left,right]
                    min_window = right - left + 1
                counter_s[s[left]] -= 1
                
                left += 1

        if min_window == float("inf"):
            return ""

        return s[index[0]:index[1] + 1]


