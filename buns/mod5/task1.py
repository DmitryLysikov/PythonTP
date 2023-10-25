class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел

class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        if self.end is None:
            return None
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        new_temp = Node(val)
        new_temp.pref = self.end
        self.end = new_temp

    def print(self):
        current_temp = self.end
        while current_temp is not None:
            print(current_temp.data)
            current_temp = current_temp.pref



stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print('Вывод до удаления элемента')
stack.print()
print('Вывод удаленного элемента')
print(stack.pop())
print('Вывод после удаления элемента')
stack.print()