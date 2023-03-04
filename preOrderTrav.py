class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorder_trav(self, root):
        res = []
        stack = [root]
        while stack:
            tmp_node = stack.pop()
            if tmp_node:
                res.append(tmp_node.val)
                stack.append(tmp_node.right)
                stack.append(tmp_node.left)
        return res

node4 = TreeNode(12, None, None)
node2 = TreeNode(1, node4, None)
node3 = TreeNode(3, None, None)
node1 = TreeNode(2, node2, node3)

res = Solution().preorder_trav(node1)
print(res)
