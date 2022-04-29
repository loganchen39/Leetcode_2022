class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        \BF algo, 2-loop, not take advantage of sorted order, not implement here.
        '''

        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        : TC: 5.41%, O(n)
        : SC: 44.15%, O(1)
        :\Two pointers with sorted order, know the pattern/rule to move the pointers.
        :\If using hash table (dict), you're not taking advantage of sorted order, SC will be O(n).
        """
        
        n = len(numbers)
        low, high = 0, n-1
        while low < high:
            if numbers[low] + numbers[high] == target:
                return [low+1, high+1]
            elif numbers[low] + numbers[high] < target:
                low += 1
            else:
                high -= 1
           
          
