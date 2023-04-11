class  Queue:
    def __init__(self) -> None:
        self.inbound_stack = []
        self.outbount_stack = []

    def enqueue(self, data):
        self.inbound_stack.append(data)
        return print(data)

    def dequeue(self):
        if not self.outbount_stack:
            while self.inbound_stack:
                self.outbount_stack.append(self.inbound_stack.pop())

        return self.outbount_stack.pop()
        

if __name__ == '__main__':
    numbers = Queue()
    numbers.enqueue(5)
    numbers.enqueue(6)
    numbers.enqueue(7)
    print(numbers.inbound_stack)
    numbers.dequeue()
    print(numbers.inbound_stack)
    print(numbers.outbount_stack)
    print(numbers.dequeue())
    print(numbers.outbount_stack)
    numbers.dequeue()
    print(numbers.outbount_stack)
    print(numbers.inbound_stack)