class Deque(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == 0

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        self.items.pop()

    def removeRear(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    d = Deque()
    d.addFront('hello')
    d.addRear('world')
    print(d.items)
    d.removeFront()
    print(d.items)
    d.removeRear()
    print(d.items)
