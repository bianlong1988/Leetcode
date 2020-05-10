"""
Option 1: Hashmap
Option 2: Same idea, one loop
Option 3: To be continued
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution1(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dic = {}
        cur_node = head

        if not head:
            return

        while cur_node:
            if cur_node not in dic:
                new_node = Node(cur_node.val, None, None)
                dic[cur_node.val] = new_node
            cur_node = cur_node.next

        node = dic[head.val]
        dummy = node
        while head:
            if head.next:
                node.next = dic[head.next.val]
            if head.random:
                node.random = dic[head.random.val]
            head, node = head.next, node.next
        return dummy


class Solution2(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dic_node = {}
        dummy = cur_node = Node(0, None, None)

        if not head:
            return None

        while head:
            if head.val not in dic_node:
                new_node = Node(head.val, None, None)
                dic_node[head.val] = new_node
            cur_node.next = dic_node[head.val]
            if head.random:
                if head.random.val not in dic_node:
                    new_node = Node(head.random.val, None, None)
                    dic_node[head.random.val] = new_node
                cur_node.next.random = dic_node[head.random.val]
            cur_node = cur_node.next
            head = head.next
        return dummy.next