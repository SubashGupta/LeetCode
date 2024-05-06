# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr = head
        while curr:
            nexts = curr.next
            curr.next = prev
            prev=curr
            curr=nexts
        head = prev
        maxi = 0
        prev = None
        current = head
        while current:
            maxi = max(maxi, current.val)
            if current.val < maxi:
                prev.next = current.next
                deleted = current
                current=current.next
                deleted.next = None
            else:
                prev = current
                current = current.next
        prev=None
        curr = head
        while curr:
            nexts = curr.next
            curr.next = prev
            prev=curr
            curr=nexts
        return prev