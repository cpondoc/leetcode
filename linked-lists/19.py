# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # General Idea: Count number of nodes, then find the node we want to delete, then go from there
        # Run-time: O(n)
        # Memory: O(1)
        front = head
        counter = 0
        while (front):
            counter += 1
            front = front.next
        node_num = counter - n
        front, prev = head, head
        counter = 0
        while (counter < node_num):
            counter += 1
            prev = front
            front = front.next
        prev.next = front.next
        if (prev == front):
            return front.next
        return head
        