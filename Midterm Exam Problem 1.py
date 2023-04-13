class Circle:
    def __init__(self, radius):
        self.radius = radius

    def radius(self):
        return float(input(self.radius()))

    def area(self):
        return 3.1416 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.1416 * self.radius

    def display(self):
        print("Area: ", self.area())
        print("Perimeter: ", self.perimeter())

radius = Circle(float(input("Radius: ")))
radius.display()