class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        :\1. Algo. 1, iteration with two-pass while-loop, First pass to find the location/pointers to left, 
        : right and left_prev, right_next, then reverse linked list of [left, right], finally reconnect all parts.
        : TC: O(n), 30.05%, 
        : SC: O(1), 51.50%, 
        '''
        
        if left==right: return head
        
        idx, prev, curr = 1, None, head
        pl, pr = None, None
        left_prev, right_next = None, None
        while curr:
            if idx==left:
                pl = curr
                left_prev = prev
            if idx==right:
                pr = curr
                right_next = pr.next
                pr.next = None
                break
            
            idx += 1
            prev = curr
            curr = curr.next
        
        prev, curr = None, pl
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
                
        if left_prev:
            left_prev.next = prev
        else:
            head = prev
        
        pl.next = right_next
        
        return head
    
    
