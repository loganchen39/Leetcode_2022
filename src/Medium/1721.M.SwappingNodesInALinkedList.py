# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        :\1. Algo. 1, BF two-pass, first count the number of nodes, then swap.
        : TC: O(n), 44.21%
        : SC: 0(1), 87.04%
        '''
        
        n, pt = 0, head
        
        while pt:
            n += 1
            pt = pt.next
        
        p1, p2 = None, None
        i, pt = 1, head
        while pt:
            if i == k:
                p1 = pt
            if i == n-k+1:
                p2 = pt
            if p1 and p2:
                break
            
            pt = pt.next
            i += 1
        
        v = p1.val
        p1.val = p2.val
        p2.val = v
        
        return head
    
    
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        :\Algo. 2, one-pass while-loop, keep track of the pt2, i.e. the kth node from last 
        : node, this trick is used in other problems.
        : TC: O(n), 96.79%
        : SC: 0(1), 57.41%
        '''
        
        i, pt, pt1, pt2 = 1, head, None, head
        
        while pt:
            if i == k:
                pt1 = pt
            if i > k:
                pt2 = pt2.next
            i += 1
            pt = pt.next
        
        v = pt1.val
        pt1.val = pt2.val
        pt2.val = v
        
        return head
    
    
