from Node import Node

class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0

    def  append(self, data):
        node = Node(data)

        if self.tail == None:
            self.tail = node
        else: 
            current = self.tail

            while current.next:
                current = current.next

            current.next = node

        self.size += 1

    def Size(self):
        return str(self.size)
    
    def iter(self):
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.tail
        previus = self.tail

        while current:
            if current.data == data:
                if current == current.next:
                    self.tail = current.next
                else:
                    previus.next = current.next
                    self.size -=1
                    return current.data
            previus = current
            current = current.next

    def search(self , data):
        for node in self.iter():
            if data == node:
                print(f"Data {data} found!")


    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0


if __name__ == '__main__':
    words = SinglyLinkedList()
    words.append('egg')
    words.append('ham')
    words.append('spam')
    current = words.tail
    while current:
        print(current.data)
        current = current.next

    for word in words.iter():
        print(word)

    words.search('spam')
    words.search('juice')
    print(words.Size())