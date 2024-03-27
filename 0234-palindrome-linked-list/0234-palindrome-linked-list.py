# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        x = head
        op = str(x.val)
        while x.next:
            op+=str(x.next.val)
            x=x.next
        return op == op[::-1]
        