# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            p1=head
            p2=head
        else:
            return False
        while p1.next and p2.next:
            p1=p1.next
            if p2.next.next:
                p2=p2.next.next
            else:
                return False
            if p1 == p2:
                return True
        return False        