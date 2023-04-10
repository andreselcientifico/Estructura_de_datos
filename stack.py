from Node import Node


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else: 
            self.top = node
        
        self.size += 1
    
    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            return data
        else: 
            return "The stack is empty"
        
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "The stack is empty"
        
    def clear(self):
        while self.top:
            self.pop()


if __name__ == '__main__':
    food = Stack()
    print(food.push('egg'),
    food.push('ham'),
    food.push('spam'),
    food.pop())
    print(food.peek())
    food.clear()
    print(food.peek())