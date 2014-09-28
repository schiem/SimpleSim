import random

class Plant:
    def __init__(self, death_age, proliferation, space_req, energy_supplied,  x, y, ID, world):
        self.genes = { "death_age" : death_age,\
            "proliferation" : proliferation,\
            "space_req" : space_req
        }

        self.world = world
        self.ID = ID
        self.energy_supplied = energy_supplied
        self.age = 0
        self.timer = 0
        #plants can all move the same speed.
        self.x = x
        self.y = y
        
        self.speed = 5
        self.is_dead = False

    def act(self, ms):
        self.timer += ms
        while(self.timer > (1/self.speed)*1000):
            self.timer -= ms
            if(self.will_proliferate()):
                self.proliferate()
        self.age += 1
        if(random.randint(0, self.genes['death_age'] - self.age) == 0):
            self.die()

    def proliferate(self):
        x, y = self.find_valid_coords(self.x, self.y)
        if(x is not None and y is not None):
            offspring = Plant(self.genes["death_age"],\
                self.genes["proliferation"],\
                self.genes["space_req"],\
                self.energy_supplied,\
                x,
                y,
                None,
                self.world)
            ID = self.world.get_id(offspring)
            if(ID is None):
                ID = self.world.generate_new_id(Plant)
            offspring.ID = ID
            self.world.mutate_organism(offspring)
            self.world.add_object(offspring)

    def die(self):
        self.is_dead = True

    def find_valid_coords(self, x, y):
        good_x = None
        good_y = None
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if(self.world.empty_space(i, j)):
                    good_x, good_y = i, j
        return good_x, good_y

    def will_proliferate(self):
        lets_go = random.randrange(self.genes['proliferation']) == 0
        space = self.empty_spaces(self.x, self.y) >= self.genes['space_req']
        return lets_go and space

    def empty_spaces(self, x, y):
        count = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                count += self.world.empty_space(i, j)
        return count
