class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data

    def remove(self, index):
        if index < 0:
            raise IndexError("Индекс выходит за пределы диапазона")
        if index == 0:
            if self.head is not None:
                self.head = self.head.next
                return
        current = self.head
        prev = None
        count = 0
        while current and count < index:
            prev = current
            current = current.next
            count += 1

        if count == index and current:
            prev.next = current.next
        else:
            raise IndexError("Индекс выходит за пределы диапазона")

    def get(self, index):
        if index < 0:
            raise IndexError("Индекс выходит за пределы диапазона")
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1
        raise IndexError("Индекс выходит за пределы диапазона")

    def insert(self, index, value):
        if index < 0:
            raise IndexError("Индекс выходит за пределы диапазона")
        if index == 0:
            node = Node(value)
            node.next = self.head
            self.head = node
            return
        current = self.head
        count = 0
        while current and count < index:
            if count == index - 1:
                node = Node(value)
                node.next = current.next
                current.next = node
                return
            current = current.next
            count += 1
        raise IndexError("Индекс выходит за пределы диапазона")

myList = LinkedList()
myList.push(5)
myList.push(6)
myList.push(8)
print("ДО удаления и замены элемента")
for item in myList:
    print(item)

myList.remove(1)
myList.insert(1, 1)
print("После")
for item in myList:
    print(item)
