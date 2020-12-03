class Solution():
    def findMedianSortedArrays(self, nums1, nums2):
        # nums1:....
        n1, n2 = len(nums1),len(nums2)
        lo, hi = 0, n1
        # if odd, kth element is the mean; if even, k and k+1 will be used to calculate mean
        k = (n1 + n2 + 1)//2 
        while lo < hi:
            # m1 elements + m2 elements = k elements
            m1 = lo + (hi - lo)//2  # 2
            m2 = k - m1  # k = 5, m1 = 2
            # if l1 > r2:
            if nums1[m1] < nums2[m2 - 1]:
                lo = m1 + 1
            else:
                hi = m1

        m1 = lo
        m2 = k - m1


        


if __name__== '__main__':
    nums1 = [1,3,5,9,11]
    nums2 = [2,4,12,13,14]
    #             l1  r1
    # nums1 = [1 3 5| 9 11]    l1 < r2
    # nums2 = [2 4 |12 13 14]  l2 < r1
    #            l2 r2
    #[1 2 3 4 5 | 9 11 12 13 14]
    #         k   m
    #        m-1