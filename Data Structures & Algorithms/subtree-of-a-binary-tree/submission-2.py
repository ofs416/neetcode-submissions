# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((p, q))

        while queue:
            p, q = queue.popleft()

            if not p and not q:
                continue
        
            if not p or not q or p.val != q.val:
                return False

            queue.append((p.left, q.left))
            queue.append((p.right, q.right))
                
        return True


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        else:
            return (self.isSubtree(root.left, subRoot) 
                or self.isSubtree(root.right, subRoot))


            
