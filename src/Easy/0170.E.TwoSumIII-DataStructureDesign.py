class TwoSum:
    '''
    :\Algo. 1, use hash set for fast check existing element and insertion. Algo. BF use 2-loop, not implemented.
    : TC: 7.39%, O(n), 
    : SC: 70.51%, O(n) for self.array and set_existed.
    '''
    
    def __init__(self):
        self.array = []
        

    def add(self, number: int) -> None:
        self.array.append(number)
        

    def find(self, value: int) -> bool:
        set_existed = set()
        for i in range(len(self.array)):
            if value-self.array[i] in set_existed:
                return True
            else:
                set_existed.add(self.array[i])
        
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)


