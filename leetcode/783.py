'''
给定一个二叉搜索树的根结点 root, 返回树中任意两节点的差的最小值。

示例：

输入: root = [4,2,6,1,3,null,null]
输出: 1
解释:
注意，root是树结点对象(TreeNode object)，而不是数组。

给定的树 [4,2,6,1,3,null,null] 可表示为下图:

          4
        /   \
      2      6
     / \
    1   3

最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
注意：

二叉树的大小范围在 2 到 100。
二叉树总是有效的，每个节点的值都是整数，且不重复。
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def get_root_list(root):
            root_list = [root.val]

            if root.left:
                x = get_root_list(root.left)
                if x:
                    root_list.extend(x)
            if root.right:
                y = get_root_list(root.right)
                if y:
                    root_list.extend(y)

            return root_list

        rst = get_root_list(root)
        rst.sort()
        min_diff = 100
        for i in range(len(rst) - 1):
            diff = rst[i + 1] - rst[i]
            if diff < min_diff:
                min_diff = diff

        return min_diff

