class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        index = {}
        for i in range(len(list1)):
            index[list1[i]] = i

        mini = float("inf")

        for j in range(len(list2)):
            if list2[j] in index:
                ssum = j + index[list2[j]]
                
                if ssum < mini:
                    mini = ssum
                    res = []
                    res.append(list2[j])
                elif ssum == mini:
                    res.append(list2[j])
                    
        return res


