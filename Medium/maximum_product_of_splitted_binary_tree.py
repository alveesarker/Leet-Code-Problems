# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        MOD = 10**9 + 7
        max_val = 0
        def sum_node_val(node):
            if node is None:
                return 0
            return node.val + sum_node_val(node.left) + sum_node_val(node.right)
        
        sum_all_node = sum_node_val(root)


        def post_order_travarse(node):
            nonlocal max_val
            if node is None:
                return 0
            
            left = post_order_travarse(node.left)
            right = post_order_travarse(node.right)

            sub_sum = node.val + left + right
            max_val = max(max_val, sub_sum * (sum_all_node - sub_sum))

            return sub_sum
        post_order_travarse(root)
        return max_val % MOD
