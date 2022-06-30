# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # General Idea: Just iterate and keep a set, to see which ones.
        # Runtime: O(n) -- because look-up in a set is constant
        # Memory: O(n) -- all elements are distinct
        seen = set()
        front, prev = head, head
        while (front):
            if front.val not in seen:
                seen.add(front.val)
                prev = front
                front = front.next
            else:
                prev.next = front.next
                front = front.next
        return head