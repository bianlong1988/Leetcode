"""
Option1 : Two pass
Option2: One pass
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = first = ListNode(0)
        dummy.next = temp = head
        length = 0
        while temp:
            temp = temp.next
            length = length + 1
        length = length - n
        while length > 0:
            length = length - 1
            first = first.next
        first.next = first.next.next
        return dummy.next

class Solution2(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = fast = slow = ListNode(0)
        dummy.next = head
        counter = 0
        while counter < n:
            fast = fast.next
            counter = counter + 1
        while fast.next:
            fast , slow = fast.next , slow.next
        slow.next = slow.next.next
        return dummy.next