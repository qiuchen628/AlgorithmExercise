class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pruneTree(self, root: TreeNode) -> TreeNode:
    if not root:
        return None
    root.left = self.pruneTree(root.left)
    root.right = self.pruneTree(root.right)
    if root.left or root.right or root.val == 1:
        return root
    else:
        return None