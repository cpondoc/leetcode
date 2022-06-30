# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # General idea: iterate through both linked lists, and then put all the nodes together 1 by 1
        # Optimization: Just append the end of the sorted node instead of reinserting all of them again
        # Run-Time: O(n) -- n is combined length of both linked lists
        # Memory: O(n) if I create new nodes, O(1) if I just stitch them together
        final = ListNode()
        counter = final
        while (list1 != None and list2 != None):
            if (list1.val < list2.val):
                counter.next = ListNode(list1.val, None)
                counter = counter.next
                list1 = list1.next
            else:
                counter.next = ListNode(list2.val, None)
                counter = counter.next
                list2 = list2.next
        while (list1 != None):
            counter.next = ListNode(list1.val, None)
            counter = counter.next
            list1 = list1.next
        while (list2 != None):
            counter.next = ListNode(list2.val, None)
            counter = counter.next
            list2 = list2.next
        return final.next