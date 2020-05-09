"""
Option1: brute force
Option2: O(n^2)
Option3: O(n)
Option4:
"""
class Solution1(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        abcabcbb
        01234567
        """
        max_len = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if self.hasNoRepeatChars(s[i: j + 1]):
                    max_len = max(max_len, j - i + 1)
        return 1 if max_len == 0 else max_len

    def hasNoRepeatChars(self,s):
        dic = {}
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                return False
        return True


class Solution2(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        i, j = 0, 0
        while i < len(s):
            hashset = set(s[i])
            j = i + 1

            while j < len(s):
                if s[j] not in hashset:
                    hashset.add(s[j])
                    max_len = max(max_len, j - i + 1)
                else:
                    break
                j += 1

            i += 1
        return 1 if max_len == 0 else max_len


class Solution3(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        
        max_len = 0
        hashSet = set()
        i, j = 0, 0
        while i < len(s) and j < len(s):
            if s[j] not in hashSet:
                hashSet.add(s[j])
                max_len = max(max_len, j - i + 1)
                j += 1
            else:
                hashSet.remove(s[i])
                i += 1
        return max_len


