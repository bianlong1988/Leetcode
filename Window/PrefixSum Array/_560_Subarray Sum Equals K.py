"""
Option 1: Brute force
Option 2: Optimized solution (create a sum array)
Option 3: Same as Option2 without extra space
Option 4: Hashmap + prefix sum
"""
# Option 1 : prefix sum
class Solution1(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sum(nums[i: j + 1]) == k:
                    counter += 1
        return counter

class Solution2(object):
    def subarraySum(self, nums, k):
        """
        [1, 1, 1]
        [0, 1, 2, 3]numSum
        :param nums:
        :param k:
        :return:
        """
        counter = 0
        numSum = (len(nums) + 1) * [0]
        for i in range(1, len(nums) + 1):
            numSum[i] = numSum[i - 1] + nums[i - 1]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if numSum[j] - numSum[i] == k:
                    counter += 1
        return counter


class Solution3(object):
    def subarraySum(self, nums, k):
        counter = 0
        for i in range(len(nums)):
            numSum = 0
            for j in range(i, len(nums)):
                numSum = numSum + nums[j]
                if numSum == k:
                    counter += 1
        return counter


class Solution4(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        [1, 1, 1]
        [0, 1, 2, 3]  Sum

        """
        count = 0
        dic = {0: 1}  # sum: freq
        curSum = 0
        for num in nums:
            curSum += num
            if curSum - k in dic:
                count += dic[curSum - k]
            dic[curSum] = dic.get(curSum, 0) + 1
        return count
