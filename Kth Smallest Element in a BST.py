# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        arr = []
        def traverseTree(root):
            if root :
                traverseTree(root.left)
                arr.append(root.val)
                traverseTree(root.right)
        traverseTree(root)
        return arr[k-1]
        

# Java 1ms Solution:

# /**
#  * Definition for a binary tree node.
#  * public class TreeNode {
#  *     int val;
#  *     TreeNode left;
#  *     TreeNode right;
#  *     TreeNode() {}
#  *     TreeNode(int val) { this.val = val; }
#  *     TreeNode(int val, TreeNode left, TreeNode right) {
#  *         this.val = val;
#  *         this.left = left;
#  *         this.right = right;
#  *     }
#  * }
#  */
# class Solution {
#     public int kthSmallest(TreeNode root, int k) {
        
#         List<Integer> arr = new ArrayList<Integer>();
#         traverseTree(root,arr);
#         return arr.get(k-1);
#     }
    
#     public static void traverseTree(TreeNode root, List<Integer> arr){
#             if (root !=  null) {
#                 traverseTree(root.left,arr);
#                 arr.add(root.val);
#                 traverseTree(root.right,arr);
#             }
#         }
    
# }

