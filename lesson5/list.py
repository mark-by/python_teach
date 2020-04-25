class Node:
    def __init__(self, element=0):
        self.element = element
        self.next = None

    # def __str__(self):
    #     return f"key: {self.element}"

class List:
    def __init__(self):
        self.root = None

    def add(self, element):
        if self.root:
            temp = self.root
            while temp.next:
                temp = temp.next
            temp.next = Node(element)
        else:
            self.root = Node(element)

    def insert(self, idx, element):
        if self.root is None:
            return
        temp_node = Node(element)
        if idx == 0:
            temp_node.next = self.root
            self.root = temp_node
            return
        curr_idx = 0
        temp = self.root
        while curr_idx < idx - 1 and temp.next:
            temp = temp.next
            curr_idx += 1
        if temp.next is None:
            return
        temp_node.next = temp.next
        temp.next = temp_node

    def print(self):
        temp = self.root
        while temp:
            print(temp.element)
            temp = temp.next

    def find(self, key):
        temp = self.root
        if self.root is None:
            return None
        while temp is not None and temp.element != key:
            temp = temp.next
        return temp

    def delete(self, key):
        if self.root is None:
            return
        temp = self.root
        if temp.element == key:
            self.root = temp.next
            del temp
            return
        while temp.next is not None and temp.next.element != key:
            temp = temp.next
        if temp.next is None:
            return
        to_delete = temp.next
        temp.next = temp.next.next
        del to_delete
