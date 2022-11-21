"""
Given a linked list where in addition to the next pointer, each node has a child pointer, which may or may not point to a separate list.
These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in below figure.
You are given the head of the first level of the list. Flatten the list so that all the nodes appear in a single-level linked list.
You need to flatten the list in way that all nodes at the first level should come first, then nodes of second level, and so on.

head -> 10 -> 5 -> 12 -> 7 > 11
         ↓               ↓
         4 -> 20 -> 13   17 -> 6
               ↓     ↓    ↓
               2    16    9
                    ↓     ↓
                    3     19 -> 15

output: 10 5 12 7 11 4 20 13 17 6 2 16 9 8 3 19 15

"""
import collections


class Node:
    def __init__(self, val=0, next=None, children=None):
        self.val = val
        self.next = next
        self.children = children


class Solution():
    def flatten_list(self, node=Node(0)):
        temp = collections.deque([])
        cur_node = head = node
        while cur_node:
            if cur_node.children:
                temp.append(cur_node.children)

            if not cur_node.next and temp:
                cur_node.next = temp.popleft()
            cur_node = cur_node.next
        return head

    def printList(self, node=Node()):
        while node:
            print("Cur Node value is %s, " % node.val)
            node = node.next


if __name__ == "__main__":
    head = Node(val=10, next=Node(5, next=Node(12, next=Node(7, next=Node(11),
                                                             children=Node(17, next=Node(6),
                                                                           children=Node(9,
                                                                                         children=Node(19, next=Node(15))))))),

                children=Node(4, next=Node(20, next=Node(13,
                                                         children=Node(16,
                                                                       children=Node(3))),
                                           children=Node(2)))
                )
    # solution = Solution().printList(head)
    solution = Solution()
    head = solution.flatten_list(head)
    solution.printList(head)
