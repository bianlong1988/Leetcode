"""
Option 1: brute force
Option 2: recursive
Option 3: Reverse second half
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution3(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        start = slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        end = self.reverse(slow)

        while start and end:
            if start.val != end.val:
                return False
            start, end = start.next, end.next
        return True

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

