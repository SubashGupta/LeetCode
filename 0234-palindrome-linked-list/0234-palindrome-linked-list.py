# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reversel(self, head: Optional[ListNode]):
        prev=None
        start=head
        while start:
            val=start.next
            start.next = prev
            prev=start
            start=val
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next

        secondhalf = self.reversel(slow.next)
        slow.next = None
        while head and secondhalf:
            if head.val != secondhalf.val:
                return False
            secondhalf=secondhalf.next
            head=head.next
        return True