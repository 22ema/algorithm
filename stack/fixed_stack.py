class FixedStack:

    class Empty(Exception):
        pass
    class Full(Exception):
        pass

    def __init__(self, capacity=256):
        self.stk = [None]*capacity
        self.capacity = capacity        ## stack size
        self.ptr = 0

    def __len__(self):
        return self.ptr

    def is_empty(self):
        return self.ptr <= 0

    def is_full(self):
        return self.ptr >= self.capacity

    def push(self, value):
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr+=1

    def pop(self):
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr-=1
        return self.stk[self.ptr]

    def peek(self):
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]

    def clear(self):
        self.ptr=0

    def find(self, value):
        if self.is_empty():
            raise FixedStack.Empty
        while True:
            if self.ptr <= 0:
                break
            else:
                if self.stk[self.ptr] == value:
                    return self.stk[self.ptr]
                else:
                    self.ptr -= 1
    def count(self, value):
        count = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                count += 1
        return count