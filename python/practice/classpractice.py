import math

class shape:
    def area(self):
        return 0
    def perimeteter(self):
        return 0

class rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area = self.width * self.height
        return area
    def perimeter(self):
        perimeter = (self.width * 2) + (self.height * 2)
        return perimeter

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pow(self.radius,2) * math.pi
        return area

    def perimeter(self):
        perimeter = (2*self.radius*math.pi)
        return perimeter

def total_area(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.area()

    return "the total area is: " + str(total_area)

def total_perimeter(shapes):
    total_perim = 0
    for shape in shapes:
        total_perim += shape.perimeter()

    return "The total perimeter is: " + str(total_perim)

shapes = [
rectangle(10,20),
circle(3)
]

print total_area(shapes)
print total_perimeter(shapes)

"""
class person:
    def __init__(self, first, last, age =22):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return self.first + " " +self.last

    def greeting(self):
        return "Hi, my name is %s" %self.full_name

ivan = person('Ivan', 'Montero', 18)
anne = person('Anne', 'Pham', 17)
print ivan.greeting
print anne.greeting

class server:
    def _init__(self):
        #map from user's name to age
        self.data = {}

    def add(self, person):
        self.data[person.full_name] = person

    def remove(self, person):
        del self.data[person.full_name]

    def get_data(self):
        return self.data

    def get_age(self, person):
        return self.data[name]

    def get_oldest(self):
        old_age = 0
        old_name = ''
        for full_name in self.data:
            if self.data[full_name].age > old_age:
                old_age = self.data[name]
                old_name = full_name
        return name


Students = server
server.add(ivan)
server.add(anne)
print Students


class Student(person):
    def __init(arg):
        person.__init__(self, first, last, age)
        self.school = school

    def greeting(self):
        return Person.greeting(self) + " I am going to " + self.school
ivan = Student('Ivan', 'Montero', 'UW', 18)


"""
