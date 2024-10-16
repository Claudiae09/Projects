#Example 2- Class Variabels
class FIUStudent:
    minumum_grade = 93


    def __init__(self, first_name, last_name, pid, email, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.pid = pid
        self.email = email
        self.grade = grade

    def current_grade(self):
        return f"{self.first_name}\'s current grade is {self.grade}."
    def grade_message(self):
        if self.grade >= self.minimum_grade
            return f"{self.first_name} will likely get an A in this course"

# TODO: Create two instances of FIU Student

student1= FIUStudent("Claudia", "Espipnosa", 123456. "cespi119@fiu.edu",90)
student2= FIUStudent("Alice", "Johnson", 123457. "ajohnson123@fiu.edu",85)
print(student1.grade_message())
print(student2.grade_message())


print(student1.minimum_grade)
FIUStudent.minimum_grade= 85

print(student1.grade_message())
print(student2.grade_message())

student1.minimum_grade = 95

print(student2.grade_message())
print(student2.grade_message())


# example 3- INheritance
class Robot:
    def __init__(self, name, weight, battery_life, price):
        self.name = name
        self.weight = weight
        self.battery_life = battery_life
        self.price = price

    def present(self):
        return f"My name is {self.name} and my battery last {self.battery_life} hours."

robot1 = Robot("Zig", 50, 4, 399.99)
print(robot1.weight, "lbs")
print(robot1.present())

class AquaticRobot(Robot):
    def __init__(self, name, weight, battery_life, price,sensors, motors, autonomous):
        super().__init__(name, weight, battery_life, price)
        self.sensors = sensors
        self.motors = motors
        self.autonomous = autonomous

    def environment(self, waterBody):
        return f"I am a water robot that collects data in {waterBody} water."

robot2= AquaticRobot("Eco", 170,8,999.99,["temperature","oxygen"],3,True)
print(robot2.price)
print(robot2.sensors)
print(robot2.present())
print(robot2.environment("fresh"))

#Example 4- Interfaces
from abc import abstractmethod, ABC

class StreamingService(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def add_subscriber(self, username):
        pass

    @abstractmethod
    def remove_subscriber(self, username):
        pass


    def display(self):
        print("I am a streaming service")

class VideoStreaming(StreamingService):
    subscribers =[]

    def __init__(self, name,cost):
        self.name = name
        self.cost = cost

    def play(self):
        print("I p[lay movies and TV shows")

    def add_subscriber(self, username):
         self.subscribers.append(username)

    def remove_subscriber(self, username):
        self.subscribers.remove(username)

x= VideoStreaming("Netflix",20)
print(x.add_subscriber("Gregeis"))
print(x.subscribers)
print(x.add_subscriber("danielfuentes"))
print(x.subscribers)
x.display()
