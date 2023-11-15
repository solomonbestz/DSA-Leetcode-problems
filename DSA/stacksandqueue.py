from collections import deque

# data = deque()

# data.append('Solo')
# element = data.popleft()

# print(element, data)

# LIFO -> Last In Last Out
class Stack:
    def __init__(self):
        self._data = []

    def add_data(self, data):
        self._data.append(data)

    def remove_data(self):
        return self._data.pop()
    
    def show_data(self):
        print(self._data)


if __name__=='__main__':
    stack = Stack()

    stack.add_data(3)
    stack.show_data()
    stack.add_data(5)
    stack.show_data()
    stack.add_data(1)
    stack.show_data()
    stack.remove_data()
    stack.show_data()

    