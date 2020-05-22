class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

"""
  1 -> 2 -> 3 -> 4 -> None
head           rest
"""


class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        rest = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rest
