# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode],left=-inf,right=inf) -> bool:
        if root is None:
            return True
        x=root.val
        return left<x<right and self.isValidBST(root.left,left,x) and self.isValidBST(root.right,x,right)
        #可以画图，然后再每个节点旁边写她的取值范围。还是不懂就看灵神视频