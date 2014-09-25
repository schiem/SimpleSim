#####################################################################
# The World class for a simple simulation.
#
# Michael Yoder
# Schiem
# v 0.1
#####################################################################

def type_constants():
    return [Plant, Animal]

class World:
    '''
    Basic initializer for the world. Height is in arbitrary units (AU).
    Parameter: height
        The height of the world.
    Parameter: width
        The width of the world.
        '''
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.objects = []

    '''
    Creates a random animal, with values that can be varied (see Animal
    Class) from 1-10, or 1-100 in the case of death age.
    '''
    def create_random_animal(self):
        speed = random.randint(1, 10)
        size = random.randint(1, 10)
        sight = random.randint(1, 10)
        death_age = random.randint(1, 100)
        ID = generate_new_id(Animal)
        
        #future me, sorry about what I'm about to do
        diets = type_constants() 
        for i in range(random.randint(1, 2)):
           diet_type.append(diets.pop(random.randrange(len(diets))))
        
        cannibal = random.choice([True, False])
        x = random.randint(1, self.width - 1)
        y = random.randint(1, self.height - 1)

        objects.append(Animal(speed, size, death_age, ID, diet_type, cannibal, x, y, self, []))

    def get_id(self, obj):
        for animal in objects:
            if(type(animal) is Animal):
                if(same_species(obj, animal)):
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
    def same_species(animal1, animal2):
        is_same = True
        for key in animal1.genes:
            is_same = is_same and compare_stat(animal1.genes[key], animal2.genes[key])
        return is_same

    '''
    Compares two stats to see if they are within 20%.
    Parameter: stat1
        First stat to compare.
    Parameter: stat2
        Second stat to compare.
    '''
    def compare_stat(stat1, stat2):
        #is the difference more than 20%.  20% is too much
        return abs((stat1-stat2)/((stat1 + stat2)/2)) > .2 
    
    '''
    Finds the lowest ID for that type of object (Plant or Animal) that
    is not currently in use.
    Parameter: obj_type
        The type of object (currently Plant or Animal) that we should be
        looking for.
    '''
    def generate_new_id(self, obj_type):
        ID = 1
        for obj in objects:
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
        pass
    
    '''
    Accessor for the world's objects.
    '''
    def get_objects(self):
        return self.objects

    '''
    Steps through all of the objects in the world and has them act.
    '''
    def run_objects(self):
        for obj in objects:
            obj.act()
            if(obj.is_dead):
                objects.remove(obj)
    
    '''
    
    Returns the distance without the expensive sqrt operation.  This is
    because we're only ever comparing distances, we don't care how far
    it actually is.
    '''
    def get_distance(x1, y1, x2, y2):
        x_dist = x1-x2
        y_dist = y1-y2
        total_dist = x_dist**2 + y_dist**2

