/*
public class ListNode {
    int val;
    ListNode next = null;

    ListNode(int val) {
        this.val = val;
    }
}*/
public class Solution {
    public ListNode ReverseList(ListNode head) {
        if(head == null){
            return null;
        }
        ListNode nex = null;
        ListNode pre = null;
        while(head != null){
            nex = head.next;
            head.next = pre;
            pre = head;
            head = nex;
        }
        return pre;
    }
}