class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operands = ["+", "-","*", "/"]
        j = 0
        
        for i in tokens:
            if i not in operands:
                stack.append(int(i))
            else:
                if i == "+":
                    r = stack[j-2] + stack[j-1]
                    stack.pop()
                    stack.pop()
                    stack.append(r)
                elif i == "-":
                    r = stack[j-2] - stack[j-1]
                    stack.pop()
                    stack.pop()
                    stack.append(r)
                elif i == "*":
                    r = stack[j-2] * stack[j-1]
                    stack.pop()
                    stack.pop()
                    stack.append(r)
                else:
                    r = int(stack[j-2] / stack[j-1])
                    stack.pop()
                    stack.pop()
                    stack.append(r)
            
        return stack[0]

print(Solution.evalRPN(Solution, ["2","1","+","3","*"]))