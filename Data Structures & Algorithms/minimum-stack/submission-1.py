class MinStack:

    def __init__(self):
        self.queue = []
        self.min_queue = []

    def push(self, val: int) -> None:
        self.queue.append(val)
        if not self.min_queue:
            self.min_queue.append(val)
            return 

        if self.min_queue[-1] >= val:
            self.min_queue.append(val)

    def pop(self) -> None:
        latest = self.queue.pop()
        if latest == self.min_queue[-1]:
            self.min_queue.pop()
        
    def top(self) -> int:
        return self.queue[-1]
        
    def getMin(self) -> int:
        return self.min_queue[-1]
