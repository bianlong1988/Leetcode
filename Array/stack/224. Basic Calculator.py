class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = collections.deque(s)
        return self.helper(s)
    
    def helper(self, s):
        # pre_sign
        pre_sign = "+" # -
        pre_num = 0 # 1
        res = 0
        
        while s:
            
            char = s.popleft()
            
            if char.isdigit():  # take care of num >= 10
                pre_num = int(char) + pre_num * 10

            if char == '(':    # 1. the order of (
                pre_num = self.helper(s)  # 4. treat as a regular number
                
            if char in '+-)' or len(s) == 0:  # 2. end of ()
                if pre_sign == '+':
                    res += pre_num 
                else:
                    res -= pre_num 
                    
                pre_sign = char    # reset
                pre_num = 0        # reset
                
            # print (res, "res", char, "char")
            
            if char == ')':  # 3. ending condition
                return res
                
        return res