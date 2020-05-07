#https://www.youtube.com/watch?v=wfcWRAxRVBA&list=PLBZBJbE_rGRWeh5mIBhD-hhDwSEDxogDg&index=9

class Robot:
    
    #constructor
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    
    def introduce_self(self):
        print("My name is: " +  self.name)


#lage objekter uten constructor
#object 1
        
# r1 = Robot()
# r1.name = "Tom"
# r1.color = "red"
# r1.weight = 30

# #object 2 

# r2 = Robot()
# r2.name = "Jerry"
# r2.color = "blue"
# r2.weight = 40

#lage objektene via constructor istedenfor. (enklere.)
r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

#calling the function. self refererer da til riktig objekt
r1.introduce_self()
r2.introduce_self()
   
    