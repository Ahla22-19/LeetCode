class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        for i in range (len(operations)):

            if operations[i] == "--X" or operations[i] == "X--":
                operations[i] = -1
            else: 
                operations[i] = 1
        print(operations)
        return sum(operations)