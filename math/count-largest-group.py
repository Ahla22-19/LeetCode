class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        hashmap = Counter()
        for i in range(1, n + 1):
            key = sum([int(x) for x in str(i)])
            hashmap[key] += 1
        
        a = max([val for key, val in hashmap.items()])
        
        count = 0
        for key, val in hashmap.items():
            if val == a:
                count += 1

        return count