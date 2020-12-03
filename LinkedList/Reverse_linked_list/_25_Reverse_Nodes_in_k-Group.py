def reverseKGroup(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not head:
        return None

    a = b = head
    for i in range(k):
        # base case: if list not longer than k, can't reverse
        if b is None:
            return head
        b = b.next

    newHead = self.reverseLikedList(a, b)
    a.next = self.reverseKGroup(b, k)
    return newHead


def reverseLikedList(self, a, b):
    cur = a  # head
    pre = None
    while cur != b:  # stop until at node b
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt

    return pre