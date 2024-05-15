# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def swapfunction(begin, k):
            prev = None
            curr = begin
            tempcount = 0
            while curr and tempcount < k:  # Adjusted condition
                tempcount += 1
                nexts = curr.next
                curr.next = prev
                prev = curr
                curr = nexts
            return prev
        
        curr = head
        finalhead = None
        prev_group_tail = None
        while curr:
            begin = curr
            tempcount = 0
            while curr and tempcount < k:
                tempcount += 1
                curr = curr.next
            if tempcount == k:
                continuehead = swapfunction(begin, k)
                if not finalhead:
                    finalhead = continuehead
                if prev_group_tail:
                    prev_group_tail.next = continuehead
                prev_group_tail = begin
            else:
                if prev_group_tail:
                    prev_group_tail.next = begin
                break
        return finalhead