# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        L1=[]
        def cal(a: TreeNode):
            if a != None:
                L1.append(a.val)
                if a.left != None:
                    cal(a.left)
                if a.right != None:
                    cal(a.right)
        cal(root1)
        cal(root2)
        return(sorted(L1))
