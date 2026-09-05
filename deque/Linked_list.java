/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
//problem name: Delete the Middle Node of a Linked List
//time complexity: O(n)
//space complexity: O(1)
class Solution {
    public ListNode deleteMiddle(ListNode head) {
        
        if (head.next==null){
            return null;

        }
        ListNode slow=head;
        ListNode fast =head.next.next;

        while (fast!=null && fast.next!=null){
            slow=slow.next;
            fast=fast.next.next;

        }
        slow.next=slow.next.next;
    
    
    return head;
    }


}




//problem name: Odd Even Linked List
//time complexity: O(n)
//space complexity: O(1)
class Solution {
    public ListNode oddEvenList(ListNode head) {

        if (head == null) {
            return null;
        }

        ListNode odd = head;
        ListNode even = head.next;
        ListNode evenHead = even;

        while (even != null && even.next != null) {

            odd.next = even.next;
            odd = odd.next;

            even.next = odd.next;
            even = even.next;
        }

        odd.next = evenHead;

        return head;
    }
}




//problem name: Reverse Linked List
//time complexity: O(n)
//space complexity: O(1)
class Solution {
    public ListNode reverseList(ListNode head) {

        ListNode temp=head;
        ListNode prev=null;

        while(temp!=null){
            ListNode front=temp.next;
            temp.next=prev;
            prev=temp;
            temp=front;

        }

        return prev;
        
    }
}