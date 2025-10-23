# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode(0, head)
        pre = dummy
        
        for _ in range(left - 1):
            pre = pre.next
        
        curr = pre.next
        
        for _ in range(right - left):
            nextNode = curr.next
            curr.next = nextNode.next
            nextNode.next = pre.next
            pre.next = nextNode
            
        return dummy.next
