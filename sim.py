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

def init_curses():
    stdscrn = curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    return stdscrn

if __name__ == "__main__":
    
    stdscrn = init_curses()
    World = world.World(20, 20, stdscrn)
    for i in range(1):
        World.create_random_animals(50)
    for i in range(1):
        World.create_random_plants(50)
    
    while(len(World.get_objects()) != 0):
        time1 = time.time()
        World.run_world(ms_per_frame())
        time.sleep(handle_framerate(time1)/1000)
    World.die()
