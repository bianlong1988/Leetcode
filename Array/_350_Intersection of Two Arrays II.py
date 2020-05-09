"""
Option 1: hashmap
Option 2: sort (if sorted inputs) constant space
"""
import collections
class Solution1(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 < nums2:
            self.intersect(nums2, nums1)  # force nums1 to be the longer one
        res = []
        counter1 = collections.Counter(nums1)
        for i, v in enumerate(nums2):
            if v in counter1 and counter1[v] > 0:
                res.append(v)
                counter1[v] = counter1[v] - 1
        return res

class Solution2(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 < nums2:
            self.intersect(nums2, nums1) # force nums1 to be the longer one
        res = []
        nums1.sort()
        nums2.sort()
        i1, i2 = 0, 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] == nums2[i2]:
                res.append(nums1[i1])
                i1, i2 = i1 + 1, i2 + 1
            elif nums1[i1] > nums2[i2]:
                i2 = i2 + 1
            elif nums2[i2] > nums1[i1]:
                i1 = i1 + 1
        return res