class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        left = right = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        else:
            return left or right

node3 = TreeNode(21)
node4 = TreeNode(26)
node5 = TreeNode(22)
node2 = TreeNode(25)
node1 = TreeNode(23)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

test_case = Solution()
res = test_case.lowestCommonAncestor(node1, node2, node5)
print(res.val)

