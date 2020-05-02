from heap import Heap
from random import randint

a = [randint(-1000, 1000) for i in range(15)]

print(a)
h = Heap()
h.build(a)
print(a)
while not h.empty():
    print(h.pop())
