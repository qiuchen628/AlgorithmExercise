class Node(object):
    def __init__(self, val, neighbours):
        self.val = val
        self.neighbours = neighbours

class Solution(object):

    def __init__(self):
        self.visited = {}

    def clone_graph(self, node):

        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        clone_node = Node(node.val, [])

        self.visited[node] = clone_node

        if node.neighbours:
            clone_node.neighbours = [self.clone_graph(n) for n in node.neighbours]

        return clone_node



n1 = Node(1,[])
n2 = Node(2,[])
n3 = Node(3,[])
n4 = Node(4,[])
n1.neighbours = [n2]
n2.neighbours = [n3, n4]

test_case = Solution()
res = test_case.clone_graph(n1)
res2=res.neighbours[0]
print(res2.val)

