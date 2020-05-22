class Solution(object):

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # initialize successor
        successor = None

        """
        a -> b -> c -> d
        reverseN(head,3)

                last  successor
        a <- b <- c    d
        |              |
         -> -> -> -> ->
        """

        # move head n positions
        def reverseN(head, n):
            if n == 1:
                self.successor = head.next
                return head

            last = reverseN(head.next, n - 1)
            head.next.next = head
            head.next = self.successor  # used to be None, but now point to successor
            return last

        if m == 1:
            return reverseN(head, n)
        # move head m positions
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head