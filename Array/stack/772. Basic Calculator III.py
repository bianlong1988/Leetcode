class Solution:
    def calculate(self, s: str) -> int:
        dq = collections.deque(s)
        return self.helper(dq)
        
    def helper(self, s) -> int:
        stack = []
        operand = 0
        sign = '+'
        while s:
            char = s.popleft()
            if char.isdigit():
                operand = operand * 10 + int(char)
            if char == '(':
                operand = self.helper(s)
            if char in "+-*/)" or len(s) == 0:             
                if sign == "+":
                    stack.append(operand)
                elif sign == "-":
                    stack.append(-operand)
                elif sign == "*":
                    stack[-1] = stack[-1] * operand
                elif sign == "/":
                    stack[-1] = int(stack[-1] / operand)
            
                operand = 0
                sign = char
            if char == ')':
                break
            # print (char, sign, stack, s)
            
        return sum(stack)