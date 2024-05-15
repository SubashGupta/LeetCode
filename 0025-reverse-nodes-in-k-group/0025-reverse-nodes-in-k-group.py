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
            return prev, curr

        curr = head
        finalhead = None  # Initialize finalhead
        prev_group_tail = None  # Track the tail of the previous reversed group
        while curr:
            begin = curr
            tempcount = 0
            while curr and tempcount < k:  # Count nodes in the current group
                tempcount += 1
                curr = curr.next
            if tempcount == k:  # If there are enough nodes to reverse
                continuehead, next_group_head = swapfunction(begin, k)
                if not finalhead:  # If finalhead is not assigned yet
                    finalhead = continuehead
                if prev_group_tail:  # Connect the previous group to the current reversed group
                    prev_group_tail.next = continuehead
                prev_group_tail = begin
            else:  # If there are fewer than k nodes left
                if prev_group_tail:  # Connect the previous group to the remaining nodes
                    prev_group_tail.next = begin
                break  # No need to reverse further
        return finalhead