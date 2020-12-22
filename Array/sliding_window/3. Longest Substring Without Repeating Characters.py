class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = set()
        max_len = 0
        l = 0
        for r, char in enumerate(s):
            while char in window: # invalid window
                if s[l] in window:
                    window.remove(s[l])
                l += 1
            max_len = max(max_len, r - l + 1) # valid window
            window.add(char) # valid window
        return max_len