class fifo:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self):
        if self.isEmpty():
            return print("Cannot remove item from an empty queue")
        
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def display(self):
        return self.items
