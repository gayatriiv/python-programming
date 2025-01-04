class Rectangle:
    # Define constructor with attributes: length and width 
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    # Create perimeter method
    def Perimeter(self):
        return 2 * (self.length + self.width)
    
    # Create area method
    def Area(self):
        return self.length * self.width   
   
    # Create display method
    def display(self):
        print("The length of rectangle is:", self.length)
        print("The width of rectangle is:", self.width)
        print("The perimeter of rectangle is:", self.Perimeter())
        print("The area of rectangle is:", self.Area())
        
# Create a Rectangle object
myRectangle = Rectangle(7, 5)
myRectangle.display()
print("----------------------------------")
