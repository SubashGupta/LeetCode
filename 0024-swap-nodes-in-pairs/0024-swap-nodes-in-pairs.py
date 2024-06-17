# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:   
        prev = ListNode(0,head)
        temps = prev
        while prev.next and prev.next.next:
            p1=prev.next
            p2=prev.next.next
            
            p1.next=p2.next
            p2.next=p1
            prev.next = p2
            prev = p1
        return temps.next