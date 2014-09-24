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

    def generate_new_id(self, obj_type):
        #generate a new ID for a plant or animal
        #requires that the ID is not already in use
        ID = 1
        for obj in objects:
            #I know, I know...old style classes
            if isinstance(obj, obj_type):
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


