class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        winners = []
        loosers = []

        for i in range (len(matches)):
            winners.append(matches[i][0])
            loosers.append(matches[i][1])

        set_winners = set(winners)
        set_loosers = set(loosers)

        always_winner = sorted(set_winners - set_loosers)

        loosers_count = Counter(loosers)
        loose_once = sorted(player for player, lose in loosers_count.items() if lose == 1 )

        return [always_winner, loose_once]
        
       




        


        