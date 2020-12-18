class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        "abcabc"
         l
            r
        a, b, c
        """
        l = 0
        window = {}
        count = 0
        for r, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            while len(window) == 3:
                # valid window -> rest part will be valid also
                count += len(s) - r
                window[char] -= 1
                if window[char] == 0:
                    del window[char]
                l += 1

        return count
   