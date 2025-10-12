"""
Given the head of a singly linked list, return the middle node of the linked list. 
If there are two middle nodes, return the second middle node. 

Edge Cases:
    - If there is only one element in the index. 
    - If there are two elements in the middle, an even-numbered array, then return the second element of the middle
"""


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        else:
            slow = head.next
            fast = head.next.next
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

            return slow




 
