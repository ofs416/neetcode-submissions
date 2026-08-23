# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(current):

            if not current:
                return (True, math.inf, -math.inf)

            mn, mx = current.val, current.val

            if current.left:
                if current.left.val >= current.val :
                    return (False, math.inf, -math.inf)
                else:
                    valid , mnleft, mxleft = dfs(current.left)
                    if not valid or mxleft >= current.val:
                        return (False, math.inf, -math.inf)
                    mn = mnleft

            if current.right:
                if current.right.val <= current.val:
                    return (False, math.inf, -math.inf)
                else:
                    valid, mnright, mxright = dfs(current.right)
                    if not valid or mnright <= current.val:
                        return (False, math.inf, -math.inf)
                    mx = mxright

            return (True, mn, mx)


        return dfs(root)[0]