# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        :\Algo. 1, one-pass while-loop, use the trick the keep the middle node, 
        : first find the mapping relationship as (1, 1), (2, 2), (3, 2), (4, 3), (5, 3), ..., 
        : you know when to move the middle node to the next. The BF of two-pass while-loop 
        : with first count, is straightforward.
        : TC: O(n), 78.77%
        : SC: O(1), 56.14%
        '''
        
        pt, pt_mid, i = head, head, 1
        while pt:
            if i%2 == 0:
                pt_mid = pt_mid.next
            
            i += 1
            pt = pt.next
        
        return pt_mid
    
    
