# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def fun(l1, l2, l3):
            if l1 != None and l2 != None and l1.val < l2.val:
                l3.val = l1.val
                l3.next = ListNode(0,None)
                fun(l1.next, l2, l3.next)
            elif l1 != None and l2 != None:
                l3.val = l2.val
                l3.next = ListNode(0,None)
                fun(l1, l2.next, l3.next)
            elif l1 != None:
                while l1 != None:
                    l3.val = l1.val
                    if not l1.next == None:
                        l3.next = ListNode(0,None)
                    l3,l1 = l3.next, l1.next
            else:
                while l2 != None:
                    l3.val = l2.val
                    if not l2.next == None:
                        l3.next = ListNode(0,None)
                    l3,l2 = l3.next, l2.next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode: 
        if not l1:
            return l2
        if not l2:
            return l1
        
        l3 = ListNode()
        fun(l1,l2,l3)
        return l3
    
