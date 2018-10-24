public class Solution {
    public boolean IsBalanced_Solution(TreeNode root) {
        if(root == null)
            return true;
        if(Math.abs(TreeDepth(root.left) - TreeDepth(root.right)) > 1)
            return false;
        return true;
    }
    
    public int TreeDepth(TreeNode pRoot){
        if(pRoot == null){
            return 0;
        }
        return Math.max(TreeDepth(pRoot.left),TreeDepth(pRoot.right)) + 1;
    }
}