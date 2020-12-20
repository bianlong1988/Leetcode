class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        [2,2,2,1,2,2,1,2,2,2]
                 l
                           r
         0 1 2 3 4 5 6
        count: 0:6
        count: 1:6
        count: 2:6
        count: 3:6
        .
        .
        .
        """
        odd_num = 0
        l = 0
        res = 0
        count = 0
        for r, num in enumerate(nums):
            if num % 2 == 1:
                odd_num += 1
                count = 0
            while odd_num == k:
                count += 1
                if nums[l] % 2 == 1:
                    odd_num -= 1
                l += 1
            res += count
            print (res)
        return res