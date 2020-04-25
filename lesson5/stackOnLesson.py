class Stack:
    def __init__(self):
        self.buffer = []

    def push(self, element):
        self.buffer.append(element)

    def empty(self):
        return True if not self.buffer else False

    def top(self):
        return self.buffer[-1]

    def pop(self):
        return self.buffer.pop(-1)