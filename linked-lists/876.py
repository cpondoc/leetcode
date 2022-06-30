# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # General Idea: Just keep track of the number, and then calculate middle node.
        # Optimization: just use Floyd's algorithm to find middle node?
        # Run-Time: O(n)
        # Memory: O(1)
        first = head
        second = head
        count = 1
        while (first != None):
            count += 1
            first = first.next
        half = count / 2
        if (int(half) != half):
            half -= 0.5
        else:
            half -= 1
        for i in range(int(half)):
            second = second.next
        return second