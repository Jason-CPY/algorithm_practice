/*
public class TreeNode {
    int val = 0;
    TreeNode left = null;
    TreeNode right = null;

    public TreeNode(int val) {
        this.val = val;

    }

}
*/
public class Solution {
    boolean isSymmetrical(TreeNode pRoot){
        if(pRoot == null){
            return true;
        }
        return help(pRoot.left, pRoot.right);
    }
    
    boolean help(TreeNode p, TreeNode q){
        if(p == null && q == null){
            return true;
        }
        if(p != null && q != null && p.val == q.val){
            return help(p.left, q.right) && help(p.right, q.left);
        }
        return false;
    }
}