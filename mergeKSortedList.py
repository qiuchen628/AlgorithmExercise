from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def lt(self, other):
        return self.val < other.val

    ListNode.__lt__ = lt

    def mergeKLists(self, lists):
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next



lists = [None] * 3

lists[0] = ListNode(3)
lists[0].next = ListNode(5)
lists[0].next.next = ListNode(7)

lists[1] = ListNode(2)
lists[1].next = ListNode(4)
lists[1].next.next = ListNode(12)

lists[2] = ListNode(7)
lists[2].next = ListNode(26)

test_case = Solution().mergeKLists(lists)
print(test_case.next.next.val)


