# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        :\Algo. 1, BF two-pass while-loop, first count.
        : TC: O(n), 54.50%
        : SC: O(1), 70.42%
        '''
        
        pt, sz = head, 0
        while pt:
            sz += 1
            pt = pt.next
            
        if sz-n+1 == 1:  # special case to remove the 1st node
            head = head.next
            return head
        
        pt, i = head, 1
        while pt:
            # this is the previous node to the removing node, which shouldn't be the 1st node.
            # that special case is dealt with above.
            if i == sz - n:  
                pt.next = pt.next.next
                return head
            i += 1
            pt = pt.next
            
            
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        :\Algo. 2, one-pass while-loop, use a trick to record the PRVIOUS node of the NTh node from 
        : the last, n is the distance. Also used a dummy node, otherwise you need to do conditional check, 
        : if the node to be removed is the first one or not, then process accordingly.
        :\Again what we need is the previous node, not the node to be removed.
        : TC: O(n), 92.61%
        : SC: O(1), 70.42%
        '''
        
        pt_prior_rm = ListNode(0, head)
        head = pt_prior_rm
        i, pt = 0, head
        
        while pt:
            if i > n:
                pt_prior_rm = pt_prior_rm.next
            i += 1
            pt = pt.next
        
        pt_prior_rm.next = pt_prior_rm.next.next
        return head.next
    
    
