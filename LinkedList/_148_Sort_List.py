"""

"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        list = []
        while node:
            list.append([node.val, node])
            node = node.next
        list.sort(key = lambda x : x[0])
        # print list
        new_head = node = ListNode(0)
        for item in list:
            # print item[0]
            node.next = item[-1]
            node = node.next
        node.next = None
        return new_head.next



head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

solution = Solution()

node =  solution.sortList(head)
while node:
    print node.val
    node = node.next



