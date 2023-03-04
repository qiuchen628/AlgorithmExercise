import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_symmetric(self, root):
        if not root:
            return True
        dq = collections.deque([(root.left, root.right),])
        while dq:
            node1, node2 = dq.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            dq.append((node1.left, node2.right))
            dq.append((node1.right, node2.left))
        return True

    # def is_mirror(self, t1, t2):
    #     if (t1 == None and t2 == None):
    #         return True
    #     if (t1 == None or t2 == None):
    #         return False
    #     return (t1.val == t2.val) and self.is_mirror(t1.left, t2.right) and self.is_mirror(t1.right, t2.left)





############################################
n1 = TreeNode(3, None, None)
n2 = TreeNode(3, None, None)
n3 = TreeNode(1, n1, n2)
test_case = Solution()
res = test_case.is_symmetric(n3)
print('the tree is symmetric: ', res)



