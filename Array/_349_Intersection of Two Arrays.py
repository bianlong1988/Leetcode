"""
Option 1: set -  bitwise operation and
Option 2: regular set and search
Option 3: sort (if sorted) constant space
"""
class Solution1(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return set1 & set2

class Solution2(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        set1 = set(nums1)
        set2 = set(nums2)
        if len(set1) < len(set2):
            self.intersection(nums2, nums1) # force set1 to be the longer one
        for item in set2:
            if item in set1:
                res.append(item)
        return res

class Solution3(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
         """
        if not nums1 or not nums2:
            return []
        if len(nums1) < len(nums2):
            self.intersection(nums2, nums1)
        res = []
        set1 = set(nums1)
        set2 = set(nums2)
        nums1 = sorted(list(set1))
        nums2 = sorted(list(set2))

        if nums2[-1] < nums1[0] or nums1[-1] < nums2[0]:
            return []
        i1, i2 = 0, 0
        while i2 < len(nums2) and i1 < len(nums1):
            print i1, i2
            if nums2[i2] == nums1[i1]:
                res.append(nums1[i1])
                i2, i1 = i2 + 1, i1 + 1
            elif nums2[i2] > nums1[i1]:
                i1 = i1 + 1
            elif nums2[i2] < nums1[i1]:
                i2 = i2 + 1
        return res