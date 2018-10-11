/**
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
    public boolean HasSubtree(TreeNode root1,TreeNode root2) {
        if(root1 == null || root2 == null){
            return false;
        }
        return judge(root1,root2) || HasSubtree(root1.left,root2) || HasSubtree(root1.right,root2);
    }
    
    public boolean judge(TreeNode p1,TreeNode p2){
        if(p2 == null){
            return true;
        }
        if(p1 == null || p1.val != p2.val){
            return false;
        }
        return judge(p1.left,p2.left) && judge(p1.right,p2.right);
    }
}