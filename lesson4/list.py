class Node :
    def __init__(self, element=0):
        self.element = element
        self.next = None

class List:
    def __init__(self):
        self.root = None

    def add(self, element):
        if self.root:
            temp = self.root
            while (temp.next):
                temp = temp.next
            temp.next = Node(element)
        else:
            self.root = Node(element)

    def print(self):
        temp = self.root
        while(temp):
            print(temp.element)
            temp = temp.next
