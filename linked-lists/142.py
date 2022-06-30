# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # General Idea: Floyd's algorithm, then for the slow pointer, we start at the place that they meet and the
        # head and then work up from there.
        # Run-Time: O(n)
        # Memory: O(1)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                slow = head
                while fast and fast.next:
                    if (slow == fast):
                        return slow
                    slow = slow.next
                    fast = fast.next
        return None