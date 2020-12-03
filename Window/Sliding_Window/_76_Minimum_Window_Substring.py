"""
Option 1. Brute force
2.
"""

# Option 1:  Did not include the duplication in the solution

class Solution1(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # S =  "ADOBECODEBANC", T = "ABC"
        # index 0123456789
        length = float("inf")
        res = ""
        s_dic = {}

        if len(t) > len(s):
            return ""
        if len(t) == len(s):
            if s == t:
                return s
        for item in s:
            s_dic[item] = 1

        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.contain(s[i:j + 1], t):
                    length = min(length, j - i + 1)
                    print i, j, length
                    if length == j - i + 1:
                        res = s[i:j + 1]
                        print res
        return res

    def contain(self, new_s, t):
        for item in t:
            if item not in new_s:
                return False
        return True


# Option 2:  Sliding Window
"""
s:      "ADOBECODEBANC"
t:               "ABC"

"""
import collections
class Solution2(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l, r, valid, start = 0, 0, 0, 0
        window = {}
        min_len = float('inf')
        dic_need = collections.Counter(t)
        while r < len(s):
            char = s[r]
            r += 1
            if char in dic_need:
                window[char] = window.get(char, 0) + 1
                if window[char] == dic_need[char]:
                    valid += 1
            print l, r, valid
            while valid == len(dic_need):
                if r - l < min_len:
                    start = l
                    min_len = r - l
                char = s[l]
                l += 1
                if char in dic_need:
                    if window[char] == dic_need[char]:
                        valid -= 1
                        window[char] -= 1
            print l, r, valid
        return '' if min_len == float('inf') else s[start : start + min_len]



answer = Solution2()
print  answer.minWindow("ADOBECODEBANC" ,"ABC")
                     #  "0123456789"
