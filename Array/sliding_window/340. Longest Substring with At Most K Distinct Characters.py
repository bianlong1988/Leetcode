#similar to 159
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        window = {}
        max_len = 0
        
        for r, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            while len(window) > k:
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] <= 0:
                        del window[s[l]]
                l+= 1    
            max_len = max(max_len, r - l + 1)
        return max_len