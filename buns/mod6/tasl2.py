class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data) - 1:
            pair = (self.data[self.index], self.data[self.index + 1])
            self.index += 2
            return pair
        elif self.index == len(self.data) - 1:
            pair = (self.data[self.index], None)
            self.index += 1
            return pair
        else:
            raise StopIteration

my_list = [5, 3, 7, 9, 1]
iterator = Iterator(my_list)

for pair in iterator:
    print(pair)