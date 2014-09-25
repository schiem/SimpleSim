#####################################################################
# The Animal class for a simple simulation.
#
# Michael Yoder
# Schiem
# v 0.1
#####################################################################

import random

class States:
    FLEE = 1
    EAT = 2
    BREED = 3
    WANDER = 4

class Animal:
    '''
    Creates an animal.  All of the attributes that can be varied in an 
    animal are taken in as parameters, as well as the x, y, world, and 
    the parents of that animal (because we can eat our parents, but we
    shouldn't eat our children, right?).
    Parameter: speed
        The speed of the animal.  I will attempt to implement it so tha
        this actually corresponds to how often the animal acts.
    Parameter: size
        The size of the animal.  Influences metabolism and what can eat
        this animal.
    Parameter: sight
        How far the animal can see.
    Parameter: death_age
        The closer in age an animal gets to death age, the more likely
        it is to randomly die.
    Parameter: ID
        The ID that is unique to each species of animal.  Animals with
        different IDs cannot breed.
    Parameter: cannibal
        Are we okay with eating our own species?
    Parameter: x
        The current x location in the world.
    Parameter: y
        The current y location in the world.
    Parameter: world
        The world we're currently in (technically, it wouldn't have to 
        be, but it is).
    Parameter: parents
        The parents, so they don't eat us.
    '''
    def __init__(self, speed, size, sight, death_age, ID, diet_type, cannibal, x, y, world, parents):
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
        self.parents = parents

        #who relies on modularity anyway?
        self.world = world

        #when energy reaches zero, you die
        self.energy = 20 
        self.max_energy = 20

        #how much energy do we give when eaten?
        #for now just size, but later more?
        self.energy_supplied = size
        self.age = 0
        self.metabolism = int(speed/size)
        self.gender = random.randint(0,1)
        self.is_dead = False
        self.refractory = 0
        self.state = States.WANDER
        self.target = None
    '''
    The core of the animal, the action.  Actions can be one of 4 things
    at the moment, which are (in order of priority): fleeing, eating,
    breeding, and meandering.
    '''
    def act(self):
        #start by setting the state
        for obj in self.world.objects_in_range(self.x, self.y, self.sight):
            if(obj.can_eat(self)):
                self.state = States.FLEE
                #if we don't have another target, this should be our target
                self.target = closer_target(obj)
            elif(self.can_eat(obj) and self.energy < (0.9 * self.max_energy)):
                self.state = States.EAT
                self.target = closer_target(obj)
            elif(self.can_breed(obj) and self.ready_to_breed() and obj.ready_to_breed()):
                self.state = States.BREED
                self.target = closer_target(obj)
            else:
                self.state = States.WANDER

        if(self.state == States.FLEE):
            self.flee(self.target.x, self.target.y)
        elif(self.state == States.EAT):
            if(self.next_to(self.target.x, self.target.y)):
                self.eat(self.target)
            else:
                self.move_towards(self.target.x, self.target.y)
        elif(self.state == States.BREED):
            if(self.next_to(self.target.x, self.target.y)):
                self.breed(self.target)
            else:
                self.move_towards(self.target.x, self.target.y)
        else:
            move(self.x + random.randint(-1, 1), self.y + random.randint(-1, 1))
            
    def next_to(self, x, y):
        next_x = abs(self.x - x) <= 1
        next_y = abs(self.y - y) <= 1
        return next_x and next_y

    def closer_target(self, new_target):
        if(self.target is None):
            return obj
        else:
            target_distance = self.world.get_distance(self.x, self.y, self.target.x, self.target.y)
            new_distance = self.world.get_distance(self.x, self.y, obj.x, obj.y)
            if(new_distance<target_distance):
                return obj
            else:
                return self.target
       

    '''
    If we see a scary thing and we have the energy, run away. Always
    first priority.
    '''
    def flee(self, x, y):
        #flee from a location
        self.x = self.x + (self.x > x) - (self.x < x)
        self.y = self.y + (self.y > y) - (self.y < y)

    '''
    If we can eat the object, then do it.  Note, this object doesn't
    have to be adjacent to us, ensuring that will be handled in act().
    '''
    def eat(self, obj):
        #eat an object
        if(can_eat(obj)):
            obj.die()
            energy = energy + obj.energy_supplied
            correct_energy()

    '''
    Locomote in the direction of a thing.
    '''
    def move_towards(self, x, y):
        #weird boolean logic
        self.x = self.x - (self.x > x) + (self.x < x)
        self.y = self.y - (self.y > y) + (self.y < y)

    '''
    Creates a new animal, but, as below, it takes two to tango.
    Ensuring that we can actually breed with the animal,that it's
    close enough, and that we WANT to breed will be handled in act(). 
    This creates a new animal with randomly combined characteristics of
    both parents, as well as mutations.
    '''
    def breed(self, animal):
        #breed with an animal
        #it takes two to tango, but both shouldn't produce offspring
        self.just_bred()
        animal.just_bred()
        #because the animal we're breeding with won't be able to breed again,
        #we can just have everything handled by this one
        
        #randomize the genes and location, a bit
        offspring_genes = self.pick_alleles(animal)
        offspring_x = self.x + random.randint(-1, 1)
        offspring_y = self.y + random.randint(-1, 1)
        
        #check to make sure the offspring isn't off the map
        if not validate_move(offspring_x, offspring_y):
            offspring_x = self.x
            offspring_y = self.y
        
        offspring = Animal(offspring_genes["speed"],\
            offspring_genes["size"],\
            offspring_genes["sight"],\
            offspring_genes["death_age"],\
            self.ID,\
            offspring_genes["diet_type"],\
            offspring_genes["cannibal"],\
            offspring_x,\
            offspring_y,\
            self.world,
            [self, animal])
        offspring.mutate_organism()
        if(world.get_id(offspring) is None):
            offspring.ID = world.generate_new_id(Animal)
        world.add_objects(offspring)

    '''
    Randomly selects which parent's genes get used.
    '''
    def pick_alleles(self, animal):
        genes = {}
        for key in self.genes:
            genes[key] = random.choice([self.genes[key], animal.genes[key]])
        return genes

    '''
    Causes slight changes to the organisms genes.
    '''
    def mutate_organism(self):
        for key in self.genes:
            if(key is not "diet_type"): 
                self.genes[key] = mutate_gene(self.genes[key])
            else:
                diets = world.type_constants() 
                diets = list(set(diets) - set(self.genes[key]))
                if(len(diets) != 0):
                    #just in case I ever add more diets...
                    self.genes[key].append(random.randrange(len(diets)))

    '''
    Changes a specific gene.
    '''
    def mutate_gene(self, gene):
        a = gene
        if(random.randint(10) == 0):
            a = a + random.randint(-1, 1)
        return a

    '''
    Sets the refractory, so that if we just bred, we don't do it again.
    Also takes energy.
    '''
    def just_bred(self):
        #let's not breed again for a while
        self.refractory = 10

        #and breeding takes quite a bit of energy...
        self.energy = energy - max_energy/2

    '''
    Checks if the animal just bred, and if it has the energy to breed again.
    '''
    def ready_to_breed(self):
        return self.refractory == 0 and energy > max_energy/2

    '''
    Will search for a specific object in sight. May be obsolete.
    '''
    def search(self, obj):
        #find any object.  Could be food, could be an animal
        pass

    '''
    Changes the current x and y, if it is inside of the map.
    Also takes energy.  Movement takes one of the animals metabolism
    cycles (it's costly!).
    '''
    def move(self, x, y):
        if(validate_move(x, y)):
            self.x = x
            self.y = y
            #it takes one metabolism tick to move
            self.energy = energy - metabolism

    '''
    Dies.
    '''
    def die(self):
        self.is_dead = True

    '''
    Checks if another animal can be bred with this one.
    We make sure that it is an animal, that it has the same ID, and that
    they're not the same gender.
    '''
    def can_breed(self, animal):
        return (type(animal) is Animal) and (animal.ID == self.ID) and (animal.gender != self.gender)

    '''
    Returns whether or not the animal can eat another object.
    '''
    def can_eat(self, obj):
        #checks if a particular object can be eaten by this animal

        #is it the same type as us?  If so, is it okay to eat it?
        cannibalize = self.ID != obj.ID or self.cannibal == True

        #Do we eat this type of object?
        dietary_restriction = type(obj) in self.diet_type 
        
        #is it too big for us to eat?
        size_restriction = self.size >= obj.size

        #let's not eat our children or potential mates, but only if we're in the mating mood
        is_child = self in obj.parents
        can_mate = can_breed(obj) and self.ready_to_breed() and animal.ready_to_breed()

        return (cannibalize and dietary_restriction and size_restriction and not is_child and not can_mate)

    '''
    Ensures that the energy cannot exceed the max energy.
    '''
    def correct_energy(self):
        if(self.energy > self.max_energy):
            self.energy = self.max_energy
    '''
    Returns whether or not a given set of coordinates is within the world.
    '''
    def validate_move(self, x, y):
        return (x <= world.width and x>=0) and (y <=world.height and y>=0)
