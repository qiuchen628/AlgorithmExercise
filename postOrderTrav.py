class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorder_trav(self, root):
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]



node4 = TreeNode(12, None, None)
node2 = TreeNode(1, node4, None)
node3 = TreeNode(3, None, None)
node1 = TreeNode(2, node2, node3)

res = Solution().postorder_trav(node1)
print(res)
