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
    public void Mirror(TreeNode root) {
        if(root != null){
            TreeNode tmp = null;
            tmp = root.left;
            root.left = root.right;
            root.right = tmp;
            if(root.left != null){
                Mirror(root.left);
            }
            if(root.right != null){
                Mirror(root.right);
            }
        }
    }
}