import random
from reduce import suma


class Array:

    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    def __random__(self,random_values):
        for i in range(len(self.items)):
            self.items[i] = random.randint(0,random_values)

    def __sum__(self):
        sumar = suma(lambda a,b: a+b, self.items)
        return sumar.suma()
    

if __name__ == '__main__':
    menu = Array(10)
    print(menu)
    menu.__random__(100)
    print(menu)
    print(menu.__sum__())