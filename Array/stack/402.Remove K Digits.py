class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []        
        for d in num:
            if len(stack) == 0 or (stack and stack[-1] <= d):
                stack.append(d)
            else:
                while(stack and stack[-1] > d and k > 0):
                    stack.pop()
                    k -= 1
                stack.append(d)
        
        while stack and k > 0:
            stack.pop()
            k -= 1
        
        for i, d in enumerate(stack):
            if d != '0':
                break
                
        res = ''.join(stack[i:]) if stack else '0'
        return res
        