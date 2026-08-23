"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {node.val: Node(node.val)}
        stack = [node]

        while stack:
            curr = stack.pop()
            for neigh in curr.neighbors:
                if neigh.val not in clones:
                    clones[neigh.val] = Node(neigh.val)
                    stack.append(neigh)
                clones[curr.val].neighbors.append(clones[neigh.val])

        return clones[node.val]
