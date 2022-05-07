# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        :\Algo. 1, move pointers and process, special cases processed first.
        : TC: O(n+m), 68.61%
        : SC: O(1), 80.73%
        '''
        
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        if list1.val <= list2.val:
            head = list1
        else:
            head = list2
            
        pt1, pt2 = list1, list2
        
        while pt1 != None and pt2 != None:
            if pt1.val <= pt2.val:
                if pt1.next: 
                    if pt1.next.val <= pt2.val:
                        pt1 = pt1.next
                    else:
                        pt1_next = pt1.next
                        pt1.next = pt2
                        pt1 = pt1_next
                else:
                    pt1_next = pt1.next
                    pt1.next = pt2
                    pt1 = pt1_next
            else:
                if pt2.next:
                    if pt2.next.val < pt1.val:  # can NOT be <= or failed. 
                        pt2 = pt2.next
                    else:        
                        pt2_next = pt2.next
                        pt2.next = pt1
                        pt2 = pt2_next
                else:
                    pt2_next = pt2.next
                    pt2.next = pt1
                    pt2 = pt2_next
        
        return head
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        :\Algo. 2, Similar to algo. 1, while-loop, the keypoint is, you gotta keep a prev pointer pointing to the 
        : current node in the merged list, and l1 and l2 pointers point to the current next nodes in list1 
        : and list2. As Tao Jing said, one of the most important trick with linked list is to use dummy node. 
        : TC: O(n+m), 60.15%
        : SC: O(1), 33.72%
        '''
        
        prehead = ListNode(-1)
        prev = prehead
        l1, l2 = list1, list2
        
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                prev = l1
                l1 = l1.next
            else:
                prev.next = l2
                prev = l2
                l2 = l2.next
        
        prev.next = l1 if l1 else l2
        
        return prehead.next
    
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        :\Algo. 3, use recursion. 
        : TC: O(n+m), 57.61%
        : SC: O(n+m) for stack for recursion, 33.72%
        '''
        
        if not list1 and not list2:  # base cases
            return None
        elif not list2:
            return list1
        elif not list1:
            return list2
        
        if list1.val <= list2.val:
            pt = self.mergeTwoLists(list1.next, list2)
            list1.next = pt
            return list1
        else:
            pt = self.mergeTwoLists(list1, list2.next)
            list2.next = pt
            return list2


