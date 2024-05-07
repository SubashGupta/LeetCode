# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.rev(head)
        curr = head
        carry=0
        while curr:
            value = (curr.val*2)+carry
            nodevalue = value%10
            curr.val = nodevalue
            carry = value//10
            if curr.next:
                curr = curr.next
            else:
                break
        if carry:
            new = ListNode(carry)
            curr.next = new
        heads = self.rev(head)
        return heads
    
    def rev(self, node:ListNode)-> ListNode:
        prev = None
        curr = node
        while curr:
            nexts = curr.next
            curr.next = prev
            prev = curr
            curr = nexts
        return prev
                
            
        