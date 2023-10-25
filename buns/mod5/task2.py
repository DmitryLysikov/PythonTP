class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def pop(self):
        """
        Возвращает элемент val из начала списка с удалением из списка
        """
        if self.start is None:
            return None
        val = self.start.data
        self.start = self.start.nref
        if self.start is None:
            self.end = None
        return val

    def push(self, val):
        """
        Добавляет элемент val в конец списка
        """
        new_temp = Node(val)
        if self.end is None:
            self.start = new_temp
        else:
            self.end.nref = new_temp
        self.end = new_temp

    def insert(self, n, val):
        """
        Вставляет элемент val между элементами с номерами n-1 и n
        """
        if n == 1:
            new_temp = Node(val)
            new_temp.nref = self.start
            self.start.pref = new_temp
            self.start = new_temp
            if self.end is None:
                self.end = new_temp
        else:
            current_temp = self.start
            for i in range(n-2):
                current_temp = current_temp.nref
            new_temp = Node(val)
            new_temp.nref = current_temp.nref
            new_temp.pref = current_temp
            current_temp.nref.pref = new_temp
            current_temp.nref = new_temp
            if new_temp.nref is None:
                self.end = new_temp

    def print(self):
        """
        Выводит содержимое очереди на экран
        """
        current_temp = self.start
        while current_temp is not None:
            print(current_temp.data)
            current_temp = current_temp.nref


queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)
queue.push(6)
print('До удаления')
queue.print()
queue.pop()
print('После удаления')
queue.print()
queue.insert(2, 10)
print('После добавления нового элемента')
queue.print()
