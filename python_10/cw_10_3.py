class Figure(object):
    def __init__(self, area=0):
        self.area = area

    def get_area(self):
        print(self.area)

class Rectangle(Figure):
    def __init__(self, length=3, width=2):
        self.length = length
        self.width = width
        super().__init__()
    
    def calculate_area(self):
        self.area = self.length * self.width

class Triangle(Figure):
    def __init__(self, base_length=4, heigth=3):
        self.base_length = base_length
        self.heigth = heigth
        super().__init__()

    def calculate_area(self):
        self.area = 0.5 * self.base_length * self.heigth 

rec = Rectangle()
tri = Triangle()

rec.calculate_area()
tri.calculate_area()

rec.get_area()
tri.get_area()
