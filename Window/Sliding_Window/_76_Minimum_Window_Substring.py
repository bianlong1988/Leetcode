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
        slow, fast = 0, 0
        charMatch = 0
        window = {}
        min_len= float("inf")
        dic_t = collections.Counter(t)
        ans = (min_len, slow, fast)
        for fast in range(len(s)):
            char = s[fast]
            window[char] = window.get(char, 0) + 1
            if window[char] == dic_t[char]:
                charMatch = charMatch + 1

            while len(dic_t) == charMatch:
                char = s[slow]
                if fast - slow + 1 < ans[0]:
                    ans = (fast - slow + 1, slow, fast)
                window[char] = window[char] - 1
                if window[char] < dic_t[char]:
                    charMatch = charMatch - 1
                slow = slow + 1
        return "" if ans[0] == float("inf") else ans[0]



answer = Solution2()
print  answer.minWindow("ADOBECODEBANC" ,"ABC")

