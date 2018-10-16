/*
public class RandomListNode {
    int label;
    RandomListNode next = null;
    RandomListNode random = null;

    RandomListNode(int label) {
        this.label = label;
    }
}
*/
public class Solution {
    public RandomListNode Clone(RandomListNode pHead){
        if(pHead == null){
            return null;
        }
        RandomListNode pCur = pHead;
        while (pCur != null)
        {
            RandomListNode node = new RandomListNode(pCur.label);
            node.next = pCur.next;
            pCur.next = node;
            pCur = node.next;
        }
         
        pCur = pHead;
        while (pCur!=null)
        {
            if (pCur.random!=null)
                pCur.next.random = pCur.random.next;
            pCur = pCur.next.next;
        }
         
        RandomListNode head = pHead.next;
        RandomListNode tmp = head;
        pCur = pHead;
        while(pCur.next!=null)
        {
            tmp = pCur.next;
            pCur.next = tmp.next;
            pCur = tmp;
        }
        return head;
    }
}