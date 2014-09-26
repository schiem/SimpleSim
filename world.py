#####################################################################
# The World class for a simple simulation.
#
# Michael Yoder
# Schiem
# v 0.1
#####################################################################
import math
import random
import sys
import curses
from animal import Animal
from plant import Plant

class World:
    '''
    Basic initializer for the world. Height is in arbitrary units (AU).
    Parameter: height
        The height of the world.
    Parameter: width
        The width of the world.
        '''
    def __init__(self, height, width, screen):
        self.height = height
        self.width = width
        self.screen = screen
        self.objects = []

    '''
    Creates a random animal, with values that can be varied (see Animal
    Class) from 1-10, or 1-100 in the case of death age.
    '''
    def create_random_animals(self, num):
        speed = random.randint(1, 10)
        size = random.randint(1, 10)
        sight = random.randint(1, 10)
        death_age = random.randint(1, 100)
        ID = self.generate_new_id(Animal)
        
        #future me, sorry about what I'm about to do
        diets = [Plant, Animal] 
        diet_type = []
        for i in range(random.randint(1, len(diets))):
           diet_type.append(diets.pop(random.randrange(len(diets))))
        
        cannibal = random.choice([True, False])
        
        for i in range(num):
            x = random.randint(1, self.width - 1)
            y = random.randint(1, self.height - 1)
        
            self.objects.append(Animal(speed, size, sight, death_age, ID, diet_type, cannibal, x, y, self, []))

    def get_animal_id(self, obj):
        for animal in self.objects:
            if(type(animal) is Animal):
                if(self.same_species(obj, animal)):
                    return animal.ID
        return None
    
    '''
    Checks if two animals are genetically similar enough to be considered
    'the same.'  They are similar enough if the difference/average of any
    given attribute results in a difference of >20%.
    Parameter: animal1
        The first animal.
    Parameter: animal2
        The second animal to compare.
    '''
    def same_species(self, animal1, animal2):
        is_same = True
        for key in animal1.genes:
            is_same = is_same and self.compare_stat(animal1.genes[key], animal2.genes[key])
        return is_same

    '''
    Compares two stats to see if they are within 20%. Returns true
    if they are within the acceptable range.
    Parameter: stat1
        First stat to compare.
    Parameter: stat2
        Second stat to compare.
    '''
    def compare_stat(self, stat1, stat2):
        #is the difference more than 20%.  20% is too much
        if(type(stat1) is int):
            return abs((stat1-stat2)/((stat1 + stat2)/2)) < .2 
        elif(type(stat1) is list):
            return len(stat1) == len(stat2)
        elif(type(stat1) is bool):
            return stat1 and stat2
        else:
            return
    
    '''
    Finds the lowest ID for that type of object (Plant or Animal) that
    is not currently in use.
    Parameter: obj_type
        The type of object (currently Plant or Animal) that we should be
        looking for.
    '''
    def generate_new_id(self, obj_type):
        ID = 1
        for obj in self.objects:
            if (type(obj) is obj_type):
                if obj.ID == ID:
                    ID = ID + 1
        return ID
        
    '''
    Adds an object to this Worlds list of objectds.
    '''
    def add_object(self, obj):
        self.objects.append(obj)

    '''
    Displays the world.  I'm not sure if I'm even going to implement this.
    '''
    def display_world(self):
        for i in range(self.height):
            line = ""
            for j in range(self.width):
                line += "."
            self.print_line(line, i)
        for obj in self.objects:
            self.print_there(obj.y, obj.x, str(obj.ID))

    def print_line(self, line, height):
        try:
            self.screen.addstr(height, 0, line)
        except curses.error:
            pass

    '''
    Print to a specific place on the terminal.
    '''
    def print_there(self, x, y, text):
        try:
            self.screen.addstr(x, y, text)
        except curses.error:
            pass
    '''
    Accessor for the world's objects.
    '''
    def get_objects(self):
        return self.objects

    def objects_in_range(self, x, y, radius):
        in_range = []
        for obj in self.get_objects():
            if(self.get_distance(obj.x, obj.y, x, y) < radius):
                in_range.append(obj)
        return in_range
    
    '''
    Steps through all of the objects in the world and has them act.
    '''
    def run_objects(self, delta_ms):
        for obj in self.objects:
            if(obj.is_dead):
                self.objects.remove(obj)
            else:
                obj.act(delta_ms)
    
    '''
    Kill the world.
    '''
    def die(self):
        curses.echo()
        curses.endwin()

    '''
    The main 'run' function.
    '''
    def run_world(self, delta_ms):
        self.run_objects(delta_ms)
        self.display_world()
        self.screen.refresh()

    
    '''
    Returns the actual distance, not just for relative comparisons.
    '''
    def get_distance(self, x1, y1, x2, y2):
        x_dist = x1-x2
        y_dist = y1-y2
        dist = math.sqrt(x_dist**2 + y_dist**2)
        return dist

    '''
    Returns the distance without the expensive sqrt operation.  This is
    because we're only ever comparing distances, we don't care how far
    it actually is.
    '''
    def get_cheap_distance(self, x1, y1, x2, y2):
        x_dist = x1-x2
        y_dist = y1-y2
        total_dist = x_dist**2 + y_dist**2
        return total_dist

    def dump_all_stats(self):
        print("Num objects: " + str(len(self.get_objects())))
        print("World: " + str(self))
        for obj in self.objects:
            obj.dump_stats()
            print("")
