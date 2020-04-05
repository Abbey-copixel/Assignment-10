class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Rectangle(Shape):
    def __init__(self,width,length):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2*(self.length + self.width)

class Square(Shape):
    def __init__(self,s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return 4*self.s1

r = Rectangle(20,30)
r.what_am_i()
sq = Square(60)
sq.what_am_i()

