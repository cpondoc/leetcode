# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # General Idea: Branch off, and make head of reversed list.
        # Runtime: O(n)
        # Memory: O(1)
        prev = None
        current = head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
            head = prev
        return head

    def reverseNaiveList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # General Idea: Create an array, and then create a new linked list from that array
        # Run-Time: O(n)
        # Memory: O(n)
        vals = []
        while (head != None):
            vals.append(head.val)
            head = head.next
        if (len(vals) == 0): return None
        new_head = ListNode()
        final = new_head
        for i in range(len(vals)):
            new_head.val = vals[len(vals) - i - 1]
            if (i < len(vals) - 1):
                new_head.next = ListNode()
                new_head = new_head.next
        return final