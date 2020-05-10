"""
Option 1: while l1 or l2
Option 2: while l1 and l2
Option 3: recursive
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def mergeTwoLists(self, l1, l2):
        dummy = node = ListNode(0)
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    node.next = ListNode(l1.val)
                    node = node.next
                    l1 = l1.next
                elif l2.val < l1.val:
                    node.next = ListNode(l2.val)
                    node = node.next
                    l2 = l2.next
            elif l1:
                node.next = ListNode(l1.val)
                l1 = l1.next
                node = node.next

            elif l2:
                node.next = ListNode(l2.val)
                l2 = l2.next
                node = node.next
                # print node.val
        return dummy.next


class Solution2:
    def mergeTwoLists(self, l1, l2):
        dummy = node = ListNode(0)
        while l1 and l2:
            if l1.val >= l2.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next
        print node.val
        if l1:
            node.next = l1
        else:
            node.next = l2
        return dummy.next

class Solution3:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else :
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
