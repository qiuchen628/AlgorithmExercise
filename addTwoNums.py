class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def add_two_numbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next

arr1 = [7, 5, 9, 4, 6]
LL1 = ListNode()
for i in arr1:
    LL1.insert(i)


arr2 = [1, 4, 2, 5, 3]
LL2 = ListNode()
for i in arr2:
    LL2.insert(i)

test_case = Solution()
res = test_case.add_two_numbers(LL1, LL2)
print(res)

