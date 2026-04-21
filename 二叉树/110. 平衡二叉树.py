# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_high(node):
            if node is None:
                return 0
            left_high=get_high(node.left)
            if left_high == -1:
                return -1
            right_high=get_high(node.right)
            if right_high == -1 or abs(left_high-right_high) > 1:
                return -1
            return max(right_high,left_high)+1
            # 我们需要真实的高度
            # 高度 = 从当前节点出发，到最远叶子节点的路径长度（节点数）
            # 判断平衡 → 需要“左右两个高度”
            # 往上返回 → 只能返回“一个高度”
            """
                 A
                / \
               B   C
                  /
                 D
                
            """

        return get_high(root)!=-1
    #源码是灵神。首先，整体框架参考的是二叉树的最大深度。因为深度是不会为负数的，所以如果它不平衡了，我们可以返回负一。就不继续往下递归了。问题是，怎么知道它不平衡呢？
    #核心代码是：abs(left_high-right_high) > 1:
    # 觉得还是难理解或许该做一下二叉树的最大深度