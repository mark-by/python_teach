from list import List

l = List()

for i in range(0, 10, 2):
    l.add(i)

l.print()

l.insert(2,25)

print("Вставили 25 на индекс 2")
l.print()

node4 = l.find(4) #вернет Node, где элемент 4
node55 = l.find(55) #вернет None
print(node4)
print(node55)

l.delete(25)
print("Удалили 25")
l.print()
