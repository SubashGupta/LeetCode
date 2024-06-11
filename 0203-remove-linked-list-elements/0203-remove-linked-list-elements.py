# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], vali: int) -> Optional[ListNode]:
        while head and head.val == vali:
            head = head.next
        curr = head
        while curr and curr.next:
            if curr.next.val == vali:
                curr.next  = curr.next.next
            else:
                curr = curr.next
        return head
        