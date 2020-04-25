class Stack:
    def __init__(self):
        self.buffer = []

    def top(self):
        size = len(self.buffer)
        if size == 0:
            return None
        return self.buffer[size-1]

    def pop(self):
        size = len(self.buffer)
        if size == 0:
            return None
        return self.buffer.pop(size-1);

    def empty(self):
        return False if len(self.buffer) > 0 else True

    def push(self, element):
        self.buffer.append(element)