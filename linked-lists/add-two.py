# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # General Idea: iterate through node by node, and keep track of the sum of the nodes and the digit + carry
        # Note: Can be modularized!
        # Runtime: O(n)
        # Memory: O(n)
        # Optimization? Can potentially do in place by adding onto the longer array/any one of the arrays, which make memory O(1)
        total = ListNode()
        total_head = total
        digit = 0
        carry = 0
        while (l1 != None and l2 != None):
            inter_sum = l1.val + l2.val + carry
            digit = inter_sum % 10
            carry = int(inter_sum / 10)
            new_node = ListNode(digit, None)
            total.next = new_node
            total = total.next
            l1 = l1.next
            l2 = l2.next
        while (l1 != None):
            inter_sum = l1.val + carry
            digit = inter_sum % 10
            carry = int(inter_sum / 10)
            new_node = ListNode(digit, None)
            total.next = new_node
            l1 = l1.next
            total = total.next
        while (l2 != None):
            inter_sum = l2.val + carry
            digit = inter_sum % 10
            carry = int(inter_sum / 10)
            new_node = ListNode(digit, None)
            total.next = new_node
            total = total.next
            l2 = l2.next
        if (carry > 0):
            new_node = ListNode(carry, None)
            total.next = new_node 
        return total_head.next