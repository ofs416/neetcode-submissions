# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return result
        q = deque([root])
        
        node_to_level = {root: 0}
        while q:
            node = q.popleft()
            
            if node:
                lvl = node_to_level[node]
                q.extend([node.left, node.right])
                node_to_level[node.left] , node_to_level[node.right] = lvl+1, lvl+1
                
                if len(result) <= lvl:
                    result.append([])
                result[lvl].append(node.val)

        return result
