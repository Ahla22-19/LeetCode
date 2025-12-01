class Solution:
    def frequencySort(self, s: str) -> str:

        ans = ''
        s_dict = dict(Counter(s))
        ss = dict(sorted(s_dict.items(),key=lambda item:item[1],reverse=True))

        for key,value in ss.items():
            ans += key*value

        return ans   


        