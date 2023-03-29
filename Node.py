class Node():
    def __init__(self, data, next=None):
        self.data = data 
        self.next = next

if __name__ == '__main__':
    node1 = None
    node2 = Node("A", None)
    node3 = Node("B", node2)
    print(node3.next.data)
    node1 = Node("C", node3)
    print(node1.next.data)
    print(node1.data)
    head = None
    for count in range(1,5):
        head = Node(count, head)
    while head != None:
        print(head.data)
        head = head.next