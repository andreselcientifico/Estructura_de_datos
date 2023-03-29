from array2 import Array
class Cube():

    def __init__(self,rows,colums, depth,fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(colums)
            for columns in range(colums):    
                self.data[row][columns] = Array(depth,fill_value)

    def get_height(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])
    
    def get_depth(self):
        return len(self.data[0][0])
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __str__(self):
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                for depth in range(self.get_depth()):
                    result += str(self.data[row][col][depth]) + " "

            result += "\n"
        return str(result)
    

if __name__ == '__main__':
    cube = Cube(3,3,3)
    print(cube)
    for row in range(cube.get_height()):
        for column in range(cube.get_width()):
            for depth in range(cube.get_depth()):
                cube[row][column][depth] = row * column * depth

    print(cube)
    print(cube.__str__())