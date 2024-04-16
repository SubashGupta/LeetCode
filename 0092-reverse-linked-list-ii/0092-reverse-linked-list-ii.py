# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count=1
        temp=head
        original=head
        prev=None
        flag=False
        start = None
        if left == right:
            return original
        while count<left:
            start=temp
            count+=1
            temp = temp.next
        end=temp
        val=temp.next
        while temp and count<=right:
            temp.next=prev
            prev=temp
            temp=val
            count+=1
            if temp:
                val = temp.next
        if count == right+1:
            end.next = temp
            if start:
                start.next = prev
            else:
                original = prev
            return original
            