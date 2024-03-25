# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        x=ListNode()
        c = x
        a=list1
        b=list2        
        while a and b:
            if a.val < b.val:
                c.next = a
                a=a.next
            else:
                c.next = b
                b=b.next
            c=c.next
        
        c.next = a or b
        return x.next