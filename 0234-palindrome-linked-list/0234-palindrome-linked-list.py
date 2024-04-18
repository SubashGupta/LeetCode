# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reversel(self, head):
        prev = None
        start = head
        while start:
            val = start.next
            start.next = prev
            prev = start
            start = val
        return prev
    
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        # Find the middle of the linked list
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        second_half_reversed = self.reversel(slow.next)
        
        # Separate the first and second halves of the linked list
        slow.next = None
        
        # Compare values of nodes in the first and reversed second half
        while head and second_half_reversed:
            if head.val != second_half_reversed.val:
                return False
            head = head.next
            second_half_reversed = second_half_reversed.next
        
        return True
