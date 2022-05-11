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
        
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        :\Algo. 2, Process directly on the original linked list to connect and reconnect, 
        : key point is to have pointers of lt_st, lt_end, ge_st, ge_end for recording the current position. 
        : TC: O(n), 42.69%
        : SC: O(1), 77.60%
        '''
        
        lt_st, lt_end, ge_st, ge_end = None, None, None, None
        pt = head
        while pt:
            if pt.val < x:
                if not lt_end:
                    if not ge_end: # lt comes first
                        lt_st, lt_end = pt, pt
                        pt = pt.next
                    else:
                        next = pt.next
                        pt.next = ge_st
                        lt_st, lt_end = pt, pt
                        head = pt
                        ge_end.next = next
                        pt = next
                else:
                    if not ge_end:
                        lt_end = pt
                        pt = pt.next
                    else:
                        next = pt.next
                        ge_end.next = next
                        lt_end.next = pt
                        lt_end = pt
                        pt.next = ge_st
                        pt = next
            else:  # pt.val >= x
                if not ge_end:
                    ge_st, ge_end = pt, pt
                    pt = pt.next
                else:
                    ge_end = pt
                    pt = pt.next
        
        if ge_end:
            ge_end.next = None
            
        return head
    
    
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        '''
        :\3. Algo. 3, Two-pointer, The power of using the dummy nodes before_head and 
        : after_head! It will reconnect pointers directly on the original list. Similar 
        : idea to Algo. 2 but a lot simpler with dummy nodes which can reduce the number of 
        : conditional checks as in Algo. 2!
        : TC: O(n), 91.65%
        : SC: O(1), 77.60%
        '''
        
        before = before_head = ListNode(0)
        after  = after_head  = ListNode(0)
        while head:
            if head.val < x:
                before.next = head
                before = head
            else:
                after.next = head
                after = head
            head = head.next
        
        after.next = None
        before.next = after_head.next
        return before_head.next
    
    
