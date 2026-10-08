class MinStack:

    def __init__(self):
        self.elements = []
        self.mins = []
        

    def push(self, val: int) -> None:
        self.elements.append(val)
        self.mins.append(min(val, self.mins[-1] if len(self.mins)>0 else float('inf')))

    def pop(self) -> None:
        val = self.elements.pop()
        self.mins.pop()
        return val

    def top(self) -> int:
        return self.elements[-1]
        
    def getMin(self) -> int:
        return self.mins[-1]

        
