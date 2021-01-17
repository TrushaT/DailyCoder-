'''
Date - 17/01/2020

Link to the problem : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/

Video link : https://www.youtube.com/watch?v=4u9oblkt_jA&feature=emb_logo

Given preorder and inorder traversal of a tree, construct the binary tree.

Related Topic - Tree , DFS

Note : Multiple solutions available 

'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
       
        def buildtree(start,end,preIndex):
            if start > end :
                return None 
            
            node = TreeNode(preorder[preIndex])
            
            inIndex = inorder.index(preorder[preIndex])
            
            node.left = buildtree(start,inIndex-1,preIndex+1)
            node.right = buildtree(inIndex+1,end,preIndex + inIndex - start +1)
            
            return node
    
        return buildtree(0,len(inorder)-1,0)
            
            