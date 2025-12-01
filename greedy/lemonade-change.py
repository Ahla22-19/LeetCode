class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        change = 0

        count5 = 0
        count10 = 0

        for i in range(len(bills)):

            change = bills[i] - 5

            if bills[i] == 5:
                count5 += 1

            elif bills[i] == 10:
                if not count5:
                    return False
                count5 -= 1
                count10 += 1

            else:
                if count5 > 0 and count10 > 0:
                    count5 -= 1
                    count10 -= 1
                   
                elif count5 >= 3:
                    count5 -= 3

                else:
                    return False

        return True    

       

        
      
        




        
        