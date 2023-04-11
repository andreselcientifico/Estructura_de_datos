
class listQueue:
    def __init__(self) -> None:
        self.items = []
        self.size = 0

    def enqueue(self, data):
        self.items.insert(0,data)
        self.size += 1
        return print(self.items)

    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data
    
    def traverse(self):
        total_items = self.size
        print(range(total_items))
        for item in range(total_items):
            print(self.items[item])

if __name__ == '__main__':
    food = listQueue()
    food.enqueue('eggs')
    food.enqueue('ham')
    food.enqueue('spam')
    print(food.dequeue())
    food.traverse()