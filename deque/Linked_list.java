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