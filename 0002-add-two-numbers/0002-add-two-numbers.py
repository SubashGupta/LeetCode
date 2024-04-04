# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = ListNode()
        curr = x
        carry=0
        while carry or l1 or l2:
            val1=0
            val2=0
            if l1:
                val1=l1.val
            if l2:
                val2=l2.val
            val = carry+val1+val2
            if val>9:
                carry = val//10
            else:
                carry = 0
            curr.next = ListNode(val%10)
            curr = curr.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return x.next
            