class Solution:

    def diameter_binary_tree(self, root):
        self.diameter = 1
        def depth(root):
            if not root:
                return 0
            ansL = depth(root.left)
            ansR = depth(root.right)
            self.diameter = max(self.diameter, ansL + ansR + 1)
            return 1 + max(ansL, ansR)

        depth(root)
        return self.diameter - 1