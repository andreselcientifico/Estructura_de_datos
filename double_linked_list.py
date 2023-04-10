

class node(object):
    def __init__(self, data , next) -> None:
        self.data = data 
        self.next = next


class TwoWayNode(node):
    def __init__(self, data, previus = None):
        node.__init__(self, data, next)
        self.previus = previus

if __name__ == '__main__':
    head = TwoWayNode(1)
    tail = head
    for data in range(2,6):
        tail.next = TwoWayNode(data, tail)
        tail = tail.next
    probe = tail
    while probe != None:
        print(probe.data)
        probe = probe.previus
     