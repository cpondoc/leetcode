# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Runtime: O(n)
        # Memory: O(1)
        
        # First, use Floyd's to find the start of the second half of the Linked List
        slow = fast = head
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        cur = slow
        if (fast != None):
            cur = slow.next

        # Reverse the Linked List
        prev = None
        current = cur
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
            cur = prev
        
        # Verify both are the same by going node by node
        while (cur != None):
            if (cur.val != head.val):
                return False
            cur = cur.next
            head = head.next
        return True
