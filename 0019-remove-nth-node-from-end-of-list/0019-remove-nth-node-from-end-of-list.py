# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        x=head
        c=0
        while x:
            c+=1
            x=x.next
        i=1
        y=head
        prev=head
        if c==n and c==1:
            return None
        if c == n:
            return head.next
        while i<c-n:
            prev = y
            y=y.next
            i+=1
        if y.next:
            y.next=y.next.next
            return head
        