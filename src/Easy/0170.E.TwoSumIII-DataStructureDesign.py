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


class TwoSum:
    '''
    :\Algo. 2, use hash table (dict) as data structure, Algo. 1 used list,
    : TC: 74.79%, add(), O(1); find(), O(n), 
    : SC: 28.37%, add(), O(n), find(), O(1),
    '''
    
    def __init__(self):
        self.data = {}
        
    def add(self, number: int) -> None:
        # self.array.append(number)
        if number in self.data: 
            self.data[number] += 1
        else:
            self.data[number] = 1
        
    def find(self, value: int) -> bool:
        for key in self.data:
            if value-key in self.data:
                if key != value-key or self.data[key] >= 2:
                    return True
        
        return False


