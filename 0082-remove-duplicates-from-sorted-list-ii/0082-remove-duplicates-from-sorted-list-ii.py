# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        x=ListNode()
        dummy = x
        temp = head.val
        flag=True
        p1=head
        p2=head.next
        while p1 and p2:
            if p2.val != p1.val:
                if flag == True:
                    x.next = ListNode(temp)
                    x=x.next
                else:
                    flag=True
                p1=p2
                p2=p2.next
                temp = p1.val
            else:
                flag= False
                p2=p2.next
        if flag:    
            x.next = ListNode(p1.val)
        return dummy.next
            
        