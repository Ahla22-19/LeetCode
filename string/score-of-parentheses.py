class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = []

        for char in s:

            if char == "(":
                stack.append("(")

            else:

                if stack[-1] == "(":
                    stack.pop()
                    stack.append("1")

                else:
                    score = 0
                    while stack and stack[-1].isdigit():
                        score += int(stack.pop())

                    stack.pop()
                    stack.append(str(int(score) * 2))

        return sum(int(i) for i in stack)



    

                




            
            
        