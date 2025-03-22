class Vehicle:
    def move(self):
        pass  

class Car(Vehicle):
    def move(self):
        print("The car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing on the water.")

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  
