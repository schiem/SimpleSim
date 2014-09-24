#####################################################################
# The Animal class for a simple simulation.
#
# Michael Yoder
# Schiem
# v 0.1
#####################################################################

import random

class Animal:
    def __init__(self, speed, size, sight, death_age, ID, diet_type, cannibal, x, y, world):
        #things we can vary
        self.genes = {"speed" : speed, \
        "size" : size, \
        "sight" : sight, \
        "death_age" : death_age,\
        "cannibal" : cannibal,\
        "diet_type" : diet_type}
        
        self.ID = ID
        self.x = x
        self.y = y
        
        #who relies on modularity anyway?
        self.world = world

        #when energy reaches zero, you die
        self.energy = 100
        self.max_energy = 100

        #how much energy do we give when eaten?
        #for now just size, but later more?
        self.energy_supplied = size
        self.age = 0
        self.metabolism = (int) speed/size 
        self.gender = random.randint(0,1)
        self.is_dead = False
        self.child = []

    def act(self):
        #do action

    def flee(self, location):
        #flee from a location

    def eat(self, obj):
        #eat an object
        if(can_eat(obj)):
            obj.die()
            energy = energy + obj.energy_supplied
            correct_energy()

    def breed(self, animal):
        #breed with an animal
        #it takes two to tango, but both shouldn't produce offspring


    def search(self, obj):
        #find any object.  Could be food, could be an animal
        

    def move(self, x, y):
        #move to a location, if it is valid
        if(validate_move(x, y)):
            self.x = x
            self.y = y

    def die(self):
        #kills the object
        self.is_dead = True

    def can_breed(self, animal):
        #checks if a particular animal can breed with this one
        return (type(animal) is Animal) and (animal.ID == self.ID) and (animal.gender != self.gender)

    def can_eat(self, obj):
        #checks if a particular object can be eaten by this animal

        #is it the same type as us?  If so, is it okay to eat it?
        cannibalize = self.ID != obj.ID or self.cannibal == True

        #Do we eat this type of object?
        dietary_restriction = type(obj) in self.diet_type 
        
        #is it too big for us to eat?
        size_restriction = self.size >= obj.size

        #let's not eat our children or potential mates
        is_child = obj in self.child
        can_mate = can_breed(obj) 

        return (cannibalize and dietary restriction and size_restriction and not is_child and not can_mate)

    def correct_energy(self):
        #change the current energy to max if we exceed the max energy
        if(self.energy > self.max_energy):
            self.energy = self.max_energy

    def validate_move(self, x, y):
        return (x <= world.width and x>=0) and (y <=world.height and y>=0)
