# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False


        queue = deque()
        queue.append((p, q))

        while queue:
            p, q = queue.popleft()

            if p.val != q.val:
                return False
        
            if p.left and q.left:
                if p.left.val == q.left.val:
                    queue.append((p.left, q.left))
                else:
                    return False
            elif p.left or q.left:
                return False

            if p.right and q.right:
                if p.right.val == q.right.val:
                    queue.append((p.right, q.right))
                else:
                    return False
            elif p.right or q.right:
                return False
        return True
        