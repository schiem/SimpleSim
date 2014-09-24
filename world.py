#####################################################################
# The Animal class for a simple simulation.
#
# Michael Yoder
# Schiem
# v 0.1
#####################################################################

class World:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.objects = []

    def create_random_animal(self):
        speed = random.randint(1, 10)
        size = random.randint(1, 10)
        sight = random.randint(1, 10)
        death_age = random.randint(1, 100)
        ID = generate_new_id(Animal)
        
        #future me, sorry about what I'm about to do
        diets = [Plant, Animal]
        for i in range(random.randint(1, 2):
           diet_type.append(diets.pop(random.randrange(len(diets))))
        
        cannibal = random.choice([True, False])
        x = random.randint(1, self.width - 1)
        y = random.randint(1, self.height - 1)

        objects.append(Animal(speed, size, death_age, ID, diet_type, cannibal, x, y)

    def get_id(self, obj):
        for animal in objects:
            if(type(animal) is Animal):
                if(same_species(obj, animal)):
                    return animal.ID
        return None

    def same_species(animal1, animal2):
        is_same = True
        for key in animal1.genes:
            is_same = is_same and compare_stat(animal1.genes[key], animal2.genes[key]
        return is_same

    def compare_stat(stat1, stat2):
        #is the difference more than 20%.  20% is too much
        return abs((stat1-stat2)/((stat1 + stat2)/2)) > .2 
    
    def generate_new_id(self, obj_type):
        #generate a new ID for a plant or animal
        #requires that the ID is not already in use
        ID = 1
        for obj in objects:
            if (type(obj) is obj_type):
                if obj.ID == ID:
                    ID = ID + 1
        return ID
        

    def add_object(self, obj):
        self.objects.append(obj)

    def display_world(self):]
        #display the wurld

    def get_objects(self):
        return self.objects

    def run_objects(self):
        for obj in objects:
            obj.act()
            if(obj.is_dead):
                objects.remove(obj)


