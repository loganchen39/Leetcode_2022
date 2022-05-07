# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        :\Algo. 1 iteratin with while-loop, centered and loop over at the "curr" node with 
        : ancillary prev and post pointers, easily figure out it's one element by one element loop. 
        : TC: O(n), 69.88%
        : SC: O(1), 56.82%
        '''
        
        if not head or not head.next:
            return head
        
        prev, curr = head, head.next
        head.next = None
        while curr:
            post = curr.next
            curr.next = prev
            prev = curr
            curr = post
        
        return prev
    
    
