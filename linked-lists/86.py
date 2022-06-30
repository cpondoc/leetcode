# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # General Idea: keep an array of all of the numbers less than  or equal to the value, 
        # appended based on order.
        # Run-time: O(n)
        # Memory: O(n)
        # Potential optimizations?
        less = []
        greater = []
        front = head
        while (front != None):
            if (front.val >= x):
                greater.append(front.val)
            else:
                less.append(front.val)
            front = front.next
        new = ListNode()
        cur = new
        arrays = [less, greater]
        for array in arrays:
            for i in range(len(array)):
                new_node = ListNode(array[i], None)
                cur.next = new_node
                cur = cur.next
        return new.next