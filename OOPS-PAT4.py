### Create a python class called circle with constructor which will take a list as an argument for the task 
### The list is [10,501,22,37,100,999,87,351]

### Create proper member variables inside the task if required and 
# use them when necessary. For example for this task 
# Create a class private variable named pi = 3.141

### From the given list create two class methods area and 
# perimeter which will be going to calculate the area and perimeter

class Circle:
    # Constructor
    def __init__(self, radius_list):
        self.radius_list = radius_list
        self.pi = 3.141  # Private variable for pi

    # Method to calculate the area
    def area(self):
        areas = []
        for radius in self.radius_list:
            area = self.pi * (radius ** 2)
            areas.append(area)
        return areas

    # Method to calculate the perimeter
    def perimeter(self):
        perimeters = []
        for radius in self.radius_list:
            perimeter = 2 * self.pi * radius
            perimeters.append(perimeter)
        return perimeters

# Test the Circle class
if __name__ == "__main__":
    radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
    circle = Circle(radius_list)
    print("Areas:", circle.area())
    print("Perimeters:", circle.perimeter())
