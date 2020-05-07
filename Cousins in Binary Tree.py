# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

# Return true if and only if the nodes corresponding to the values x and y are cousins.

# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false

# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true

# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false

# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3322/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isCousins(self, root, x, y):
        ans = []
        
        def traverse(root,n,depth_1,parent_root):
            if(root): 
                traverse(root.left,n,depth_1+1,root.val)
                traverse(root.right,n,depth_1+1,root.val)         
                if (root.val == n ):   
                    ans.append(depth_1)
                    ans.append(parent_root)
                    return
                    
        traverse(root,x,0,root.val)
        traverse(root,y,0,root.val)
        if (ans[0]==ans[2]) and (ans[1] != ans[3]) :
            return True
        return False
        

    
        
                
            

            