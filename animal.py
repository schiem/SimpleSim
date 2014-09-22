#####################################################################
# The Animal class for a simple simulation.
#
# Michael Yoder
# Schiem
# v 0.1
#####################################################################

import random

class Animal:
    def __init__(self, speed, size, death_age, ID, diet_type, animal_type, cannibal, x, y):
        self.speed = speed
        self.size = size
        self.death_age = death_age
        self.ID = ID
        self.diet_type = diet_type
        self.animal_type = animal_type
        self.cannibal = cannibal
        self.x = x
        self.y = y

        #when energy reaches zero, you die
        self.energy = 100
        self.max_energy = 100

        #how much energy do we give when eaten?
        #for now just size, but later more?
        self.energy_supplied = size
        self.age = 0
        #self.metabolism = ?
        self.gender = random.randint(0,1)

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

    def search(self, obj):
        #find any object.  Could be food, could be an animal

    def move(self, location):
        #move to a location, if it is valid

    def die(self):
        #kills the object

    def can_breed(self, animal):
        #checks if a particular animal can breed with this one
        return animal.ID == self.ID

    def can_eat(self, obj):
        #checks if a particular object can be eaten by this animal
    
    def correct_energy(self):
        #change the current energy to max if we exceed the max energy
        if(self.energy > self.max_energy):
            self.energy = self.max_energy
