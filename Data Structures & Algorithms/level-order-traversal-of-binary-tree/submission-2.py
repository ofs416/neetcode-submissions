# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        q = deque([root])
        result = [[root.val]]
        node_to_level = {root: 0}
        
        while q:
            current = q.popleft()
            lvl = node_to_level[current]


            if current.left or current.right:

                if lvl+1 not in node_to_level.values():
                    result.append([])


                if current.left:
                    q.append(current.left)
                    result[lvl+1].append(current.left.val)
                    node_to_level[current.left] = lvl + 1

                if current.right:
                    q.append(current.right)
                    result[lvl+1].append(current.right.val)
                    node_to_level[current.right] = lvl + 1

        return result
