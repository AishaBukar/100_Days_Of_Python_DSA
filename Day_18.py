# Validate BST
#Check if a tree is a valid Binary Search Tree

def isValid( root):
    if root is None:
        return True
    def dfs(left,node,right):
        if not(node.val > left and node.val < right):
            return False
        else:
            return (dfs(left,node.left,node.val) and dfs(node.val,node.right,right))
    return dfs(root, float("-inf"), float("inf"))

