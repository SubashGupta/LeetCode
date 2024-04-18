# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        x = head
        op = ""
        while x:
            op+=str(x.val)
            x=x.next
        return op == op[::-1]
        