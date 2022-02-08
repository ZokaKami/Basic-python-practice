class Rectangle:
    def __init__(self, x, y):
        self.width = x
        self.height = y

    def set_width(self, x):
        self.width = x
        print(self.width)

    def set_height(self, y):
        self.height = y
        print(self.height)

    def get_area(self):
        print(self.height * self.width)

    def get_perimeter(self):
        print((2 * self.width + 2 * self.height))

    def get_diagonal(self):
        print((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            print("Square is too big")
            return False
        i = 0
        while i < self.height:
            print("*" * self.width, end="\n")
            i += 1


class Square(Rectangle):
    def __init__(self, x):
        self.height = x
        self.width = x

    def set_side(self, x):
        self.height = x
        self.width = x
        print(str('"Square(side={})"'.format(x)))


Draw = Rectangle(25, 25)
Draw.get_area()
Draw.get_picture()
Sq = Square(10)
Sq.get_area()
Sq.set_side(11)
Sq.get_picture()
