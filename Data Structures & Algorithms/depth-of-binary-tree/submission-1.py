# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque()
        queue.append(root)
        depth = {root: 1}

        while queue:
            current = queue.popleft()

            if current.left:
                queue.append(current.left)
                depth[current.left] = depth[current] + 1
            if current.right:
                queue.append(current.right)
                depth[current.right] = depth[current] + 1

        return max(depth.values())
