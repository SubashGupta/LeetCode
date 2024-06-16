# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        while head and head.val == val:
            head=head.next
        p1=head
        while p1 and p1.next:
            if p1.next.val == val:
                p1.next=p1.next.next
            else:
                p1=p1.next            
        return head