class Solution:

    def decodeString(self, s: str) -> str:

        s_stack, n_stack = [], []
        num, cur_string = 0, ''
        for i, char in enumerate(s):
            if char.isdigit():
                num = int(char) + 10 * num
            elif char.isalpha():
                cur_string = cur_string + char
            elif char == '[':
                s_stack.append(cur_string)
                n_stack.append(num)
                num, cur_string = 0, ''       
            elif char == ']':
                pre_string = s_stack.pop()
                cur_string = pre_string + cur_string * n_stack.pop()
                
        return cur_string