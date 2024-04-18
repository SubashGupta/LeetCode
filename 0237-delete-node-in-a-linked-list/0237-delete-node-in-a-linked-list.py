# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        i=0
        while node.next is not None and node.next.next is not None:
            i+=1
            print(i)
            vali = node.next.val
            node.val = vali
            node = node.next
        if node.next.next is None:
            vali = node.next.val
            node.val = vali
            node.next = None
            
        