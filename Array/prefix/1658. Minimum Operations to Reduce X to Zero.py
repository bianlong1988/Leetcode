class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        [1,1,4,2,3]  x=4
           i.  j
        nums_sum - (cur_sum - prefix_sum) = x
                       j          i
        """
        
        prefix_sum = {0:-1}
        cur_sum = 0
        nums_sum = sum(nums)
        max_len = float('-inf')
        for i, num in enumerate(nums):
            cur_sum += num
            if cur_sum not in prefix_sum:
                prefix_sum[cur_sum] = i
            target = x - nums_sum + cur_sum
            if target in prefix_sum:
                # print (i, prefix_sum[prefix])
                max_len = max(max_len, i - prefix_sum[target])
        return -1 if max_len == float('-inf') else len(nums) - max_len
                