class Solution:
    def calculate(self, s: str) -> int:
        pre_sign = '+'
        pre_num = 0
        cur_num = 0
        res = 0
        for i, char in enumerate(s):
            if char.isdigit():
                cur_num = cur_num * 10 + int(char)
            # pre_num is used to store the result of "*/" e.g.   10 = 2  *  3    + 4
            #                                                         pre * cur
            #                                                    res +          + pre_num
            if char in "+-*/" or i == len(s) - 1:
                if pre_sign == '-':
                    res += pre_num  
                    pre_num = -cur_num
                elif pre_sign == '+':
                    res += pre_num
                    pre_num = cur_num
                elif pre_sign == "*":   # update pre_num
                    pre_num = pre_num * cur_num
                elif pre_sign == '/':  # update pre_num
                    pre_num = int(pre_num / cur_num)   
                pre_sign = char
                cur_num = 0
            # print (res, "res |", char,"char |", cur_num,"cur_num |", pre_num, "pre_num |", pre_sign, "pre_sign")

        return res + pre_num  

class Solution:

    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return 0
        stack = []
        sign = '+'
        operand = 0
        for i, char in enumerate(s):
            if char.isdigit():
                operand = operand * 10 + int(char)
            if char in "+-*/" or i == len(s) - 1:
                if sign == '+':
                    stack.append(operand)
                elif sign == '-':
                    stack.append(-operand)
                elif sign == '/':
                    pre = stack.pop()
                    stack.append(int(pre/operand))
                elif sign == '*':
                    pre = stack.pop()
                    stack.append(pre*operand)
                sign = char
                operand = 0

        return sum(stack)           
                
            
 