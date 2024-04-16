# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        dummy = start
        v1=list1
        v2=list2
        while v1!= None and v2!=None:
            if v1.val <v2.val:
                dummy.next = v1
                v1 = v1.next
            else:
                dummy.next=v2
                v2=v2.next
            dummy=dummy.next
        if v1:
            dummy.next = v1
        if v2:
            dummy.next = v2
        
        return start.next