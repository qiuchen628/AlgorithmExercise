class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_trav(self, root):
        res = []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right





node4 = TreeNode(12, None, None)
node2 = TreeNode(1, node4, None)
node3 = TreeNode(3, None, None)
node1 = TreeNode(2, node2, node3)

res = Solution().inorder_trav(node1)
print(res)
