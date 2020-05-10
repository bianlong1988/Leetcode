# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = node = ListNode(0)
        while l1 or l2:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            sum = v1 + v2 + carry
            carry = sum / 10
            node.next = ListNode(sum % 10)
            node = node.next
        if carry > 0:
            node.next = ListNode(carry)
            node = node.next
        return head.next


import unittest
class TestAddTwoNumbers(unittest.TestCase):
    def test_addTwoNumbers(self):
        result = Solution().addTwoNumbers(ListNode(2), ListNode(5))
        self.assertEqual(result.val, ListNode(7).val)
if __name__ == "__main__":
    unittest.main()
"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
ListNode(2).next = ListNode(4)
ListNode(4).next = ListNode(3)

ListNode(5).next = ListNode(6)
ListNode(6).next = ListNode(4)

ListNode(7).next = ListNode(0)
ListNode(0).next = ListNode(8)
# solution = Solution()
# print solution.addTwoNumbers(ListNode(2), ListNode(5))
# print Solution().addTwoNumbers(ListNode(2), ListNode(5))
