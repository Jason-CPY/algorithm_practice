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
    TreeNode pre=null;
    TreeNode lastLeft=null;
    
    public TreeNode Convert(TreeNode pRootOfTree) {
        if(pRootOfTree == null){
            return null;
        }
        Convert(pRootOfTree.left);
        pRootOfTree.left = pre;
        if(pre != null){
            pre.right = pRootOfTree;
        }
        pre = pRootOfTree;
        lastLeft = lastLeft == null ? pRootOfTree:lastLeft;
        Convert(pRootOfTree.right);
        return lastLeft;
    }
}