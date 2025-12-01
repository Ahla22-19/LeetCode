class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        count = defaultdict(int)
        res = 0

        for value in answers:

            if value == 0:
                res += 1  

            elif count[value] == 0: 
                count[value] = value  
                res += value + 1  

            else:
                count[value] -= 1

        return res



        


        