/*
public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}*/
public class Solution {
    public ListNode FindFirstCommonNode(ListNode pHead1, ListNode pHead2) {
        if(pHead1 == null || pHead2 == null){
            return null;
        }
        ListNode p1 = pHead1;
        ListNode p2 = pHead2;
        while(p1 != p2){
            if(p1 != null)
                p1 = p1.next;
            else
                p1 = pHead1;
            if(p2 != null)
                p2 = p2.next;
            else
                p2 = pHead2;
        }
        return p1;
    }
}