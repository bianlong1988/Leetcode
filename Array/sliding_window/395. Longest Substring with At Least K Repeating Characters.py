class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hashset = set(s)
        max_len = 0
        # call sliding window function to iterate 26 disctinct characters. => O(26*n)
        for m in range(len(hashset) + 1):
            max_len = max(max_len, self.slidingWindow(m, s, k))
        return max_len
                 
        
    def slidingWindow(self, m, s, k):
        count = 0 # how many chars satisfiy: freq >= k
        l = 0
        window = {} 
        max_len = 0
        for r, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            if window[char] == k:
                count += 1
            # print ("window before",window, "count", count)
            while len(window) > m: # exceed the required distinct characters -> invalid window
                if window[s[l]] == k: # decrement count
                    count -= 1
                #shrink window
                window[s[l]] -= 1 
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            if count == m: # when count == distinct chars
                # print (l, r, "window after",window, m)
                # print (s[l: r + 1])
                max_len = max(max_len, r - l + 1)
        return max_len