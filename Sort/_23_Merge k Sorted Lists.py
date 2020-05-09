# Definition for singly-linked list.
"""
Option 1: Sort tuple(val, node)
    Time: O(nklogn), Space O(kn)
Option 2: Compare k rows of nodes one by one
    Time: O(k*n), Space O(n)
Option 3: Min heap
    Time: O(nklogn), Space O(k*n)
"""
# Option 1:
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        temp_lst = []
        for i in range(len(lists)):
            node = lists[i]
            while node:
                temp_lst.append((node.val, node))
                node = node.next
        temp_lst.sort(key=lambda x: x[0])
        head = temp_node = ListNode(0)
        for node in temp_lst:
            temp_node.next = node[-1]
            temp_node = temp_node.next
        return head.next

#Option 3:
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for i in range(len(lists)):
            if lists[i]:  # [[]]
                heap.append((lists[i].val, lists[i]))
        heapq.heapify(heap)
        head = node = ListNode(None)
        while heap:
            val, temp_node = heapq.heappop(heap)
            node.next = temp_node
            node = node.next
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
        return head.next
