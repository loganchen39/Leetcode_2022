# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        :\1. Algo. 1, BF, create 2 ancillary lists lt and ge, and then combine them together, 
        : and it's "stable", i.e. the original order will be kept. 
        : TC: O(n), 77.08%
        : SC: O(n), 77.60%
        '''
        
        lt, ge = None, None
        pt_lt, pt_ge = lt, ge
        
        pt = head
        while pt:
            if pt.val < x:
                if not pt_lt:
                    pt_lt = ListNode(pt.val)
                    lt    = pt_lt
                else:
                    pt_lt.next = ListNode(pt.val)
                    pt_lt = pt_lt.next
            else:
                if not pt_ge:
                    pt_ge = ListNode(pt.val)
                    ge = pt_ge
                else:
                    pt_ge.next = ListNode(pt.val)
                    pt_ge = pt_ge.next
            
            pt = pt.next
        
        if not pt_lt and not pt_ge:
            return None
        elif not pt_ge:
            return lt
        elif not pt_lt:
            return ge
        else:
            pt_lt.next = ge
            return lt
        
        
