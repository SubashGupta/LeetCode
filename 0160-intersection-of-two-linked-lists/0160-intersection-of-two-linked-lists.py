# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        head1 = headA
        head2 = headB
        c1=0
        c2=0
        c=0

        while head1 or head2:
            if head1:
                c1+=1
                head1 = head1.next
            if head2:
                c2+=1
                head2 = head2.next
        diff = c1-c2
        copy1 = diff
        head1 = headA
        head2 = headB
        if diff<0:
            while diff != 0:
                head2 = head2.next
                diff+=1
        else:
            while diff != 0:
                head1 = head1.next
                diff-=1
        while head1!=None:
            if head1 == head2:
                return head1
            head1 = head1.next
            head2 = head2.next
        return head1
                
        