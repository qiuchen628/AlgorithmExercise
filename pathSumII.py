class Solution:

    def pathSum(self, root, sum):
        pathsList = []
        self.recursiveTree(root, sum, [], pathsList)
        return pathsList

    def recurseTree(self, node, remainingSum, pathNodes, pathsList):
        if not node:
            return

        pathNodes.append(node.val)

        if remainingSum == node.val and not node.left and node.right:
            pathsList.append(list(pathNodes))

        else:
            self.recurseTree(node.left, remainingSum-node.val, pathNodes, pathsList)
            self.recurseTree(node.right, remainingSum-node.val, pathNodes, pathsList)

        pathNodes.pop()


