import time

import world
import animal
import plant

if __name__ == "__main__":
    World = world.World(20, 20)
    for i in range(5):
        World.create_random_animals(2)
    while(len(World.get_objects()) != 0):
        World.run_world()
        print(World.dump_all_stats())
        #time.sleep(1)
