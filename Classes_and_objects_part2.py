#https://www.youtube.com/watch?v=WOwi0h_-dfA&list=PLBZBJbE_rGRWeh5mIBhD-hhDwSEDxogDg&index=10

class Robot:
        
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    
    def introduce_self(self):
        print("My name is: " +  self.name)
#new class
class Person:
    
    #constructor (with robotOwned argument.)
    def __init__(self, name, personality, isSitting, robotOwned):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
        self.robotOwned = robotOwned
        
    #fuctions (x2) for sitting down and standing up. Also prints what state person is in.    
    def sit_down(self):
        self.isSitting = True
        print(self.name, "is sitting")
        
    def stand_up(self):
        self.isSitting = False
        print(self.name, "is standing")
        
    #funtion for telling which robot is owned by what person. 
    #robotOwned will refer to either r1 or r2 then we add the self.name 
    def i_own(self):
        print("My name is: " +self.name, " and i own robot " +self.robotOwned.name)
    
        
r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

#object for person (notice boolean and robot owned)
p1 = Person("Alice", "aggressive", False, r2)
p2 = Person("Becky", "talkative", True, r1)

print("===========================")
r1.introduce_self()
p2.robotOwned.introduce_self()
print()
p1.i_own()
p2.i_own()
print()
p1.stand_up()
p2.stand_up()
p1.sit_down()

