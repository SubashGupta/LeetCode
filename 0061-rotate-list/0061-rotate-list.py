# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: 
        if head == None or k == 0:
            return head
        curr = head
        length = 0
        while curr:
            length+=1
            curr=curr.next
        if length == k:
            return head
        k = k%length
        tobreak = length - k
        if tobreak == length:
            return head
        c=1
        curr = head
        while c<tobreak:
            curr=curr.next
            c+=1
        breakstart = curr.next
        curr.next = None
        newhead = breakstart
        while breakstart.next!=None:
            breakstart = breakstart.next
        breakstart.next = head
        return newhead