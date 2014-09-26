import time
import curses

import world
import animal
import plant

def ms_per_frame():
    return 70

def handle_framerate(old_time):
    ms = ms_per_frame()
    new_time = time.time()
    frame_time = new_time - old_time
    if(frame_time < ms):
        return ms - frame_time
    else:
        return 10

if __name__ == "__main__":
    stdscrn = curses.initscr()
    curses.noecho()
    World = world.World(20, 20, stdscrn)
    for i in range(5):
        World.create_random_animals(6)
    while(len(World.get_objects()) != 0):
        time1 = time.time()
        World.run_world(ms_per_frame())
        time.sleep(handle_framerate(time1)/1000)
    World.die()
