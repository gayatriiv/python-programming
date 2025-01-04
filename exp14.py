class Shape:
    def area(self, side1, side2=None):
        if side2 is None:
            print(f"Area of the square: {side1 * side1}")
        else:
            print(f"Area of the rectangle: {side1 * side2}")

shape = Shape()
shape.area(5)
shape.area(5, 10)


