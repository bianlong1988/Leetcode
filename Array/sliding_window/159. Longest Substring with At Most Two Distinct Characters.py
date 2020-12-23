class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        window = {}
        max_len = 0
        for r, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            while len(window) > 2:
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] <= 0:
                        del window[s[l]]
                l += 1
            # print (r, l, window)
            max_len = max(max_len, r - l + 1)
        return max_len