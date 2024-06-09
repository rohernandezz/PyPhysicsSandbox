#simulation_on = False
simulation_on = True
##############################
from pyphysicssandbox import *
import drawBot
from random import random, randint, randrange, seed

#----------------
#General Settings:
#----------------
win_width = 2000
win_height = 1000
w,h = win_width, win_height
window('Floating_varGravity', w, h, fps=30)

gral_random_seed = 567
seed(gral_random_seed)
#-----------------------------
gravity_values = (100,-200)
gravity(gravity_values[0], gravity_values[1])       ###👈🏼👈🏼GRAVITY
resistance = .95     #sandbox default is .95
gral_elasticity = .9 #sandbox default is .9
gral_friction   = .6   #sandbox default is .6
#---------------------------------------------------


##------------
## Setup data:
##------------
'''
Setup variables, coordinates, data, etc, here:
'''
##


##-------------
## World setup:
##-------------
'''
Setup foor, walls, anchors, etc, here: ---
'''
### World variables:
floor_h = 2
floor_color = Color("Red")
wall_w =  5
wall_color = Color("Blue")
y_limit = "both"
diploe_grey   = rgb_to_normalized(218,219,238,255)
diploe_yellow = rgb_to_normalized(230,228,102,255)
###----------------------------------------
### Physicsiphy world:
left_wall  = static_box((0,0), wall_w, h)
right_wall = static_box((w-wall_w,0), wall_w, h)
left_wall.color = wall_color
right_wall.color = wall_color
#### Background
background = cosmetic_box((0, 0), w, h)
background.color = Color("Grey")
background.db_color = diploe_grey
#### Floor or ceiling: (both use floorH:int)
if y_limit == "floor":
    floor      = static_box((0, h-floor_h), w, floor_h)    
elif y_limit == "ceiling":
    ceiling    = static_box((0, 0), w, floor_h)
elif y_limit == "both":
    ceiling    = static_box((0, 0), w, floor_h)
    floor      = static_box((0, h-floor_h), w, floor_h)    
floor.color = floor_color

#### DrawBot

####------------------


##------------------------------------------------------


## Simulation Objects setup:
##--------------------------
'''
Setup sandbox objects here.----
'''

origins_a = [(100,100), (100,600),(650,350), (700,800),(1200,500), (1300,100),]
texts_a   = [ "text1",
            "Diplöe",
            "A longer text",
            "Short",
            "TWO WORDS",
            "SNIPPETS",
            "aaaa",
            "hhdsjhfajsd",]
box_dimensions   = (500, 100)
boxes_a = {}
for i,origin in enumerate(origins_a):
    boxes_a[i] = textBox_with_font(origin,box_dimensions[0],box_dimensions[1],texts_a[i],"fonts/Diploe-BoldItalic.otf",300)
    boxes_a[i].color    = Color("Yellow")
    boxes_a[i].db_color = diploe_yellow
    boxes_a[i].elasticity= gral_elasticity
    boxes_a[i].hit((20000000*randrange(-1,1),20000000*randrange(-1,1)),(origin[0]+box_dimensions[0]/2,origin[1]-box_dimensions[1]/2))
print(boxes_a)    


def gravity_change_observer(keys):
    #print(f"{gravity}")
    curr_space = boxes_a[i].space
    curr_gravity = curr_space.gravity
    set_grav_x = curr_gravity[0]+1
    set_grav_y = curr_gravity[1]+1
    
    if set_grav_x > 150:
        set_grav_y = curr_gravity[1]+15

    gravity(set_grav_x,set_grav_y)
    print(f"grav:{curr_gravity}")
    

    356.0, 2340.0

def gravity_shift(keys):
    curr_space = boxes_a[i].space
    curr_gravity = curr_space.gravity

    set_grav_x = curr_gravity[0]
    set_grav_y = curr_gravity[1]    
    
    if curr_gravity[0] > 170:
        set_grav_x = curr_gravity[0]-curr_gravity[0]*.75
        set_grav_y = curr_gravity[1]

    gravity(set_grav_x,set_grav_y)

add_observer(gravity_change_observer)
#add_observer(gravity_shift)

#boxB=(w*.1,400,w*.8,220)
#box_b = textBox_with_font((boxB[0], boxB[1]),boxB[2],boxB[3],"my text","fonts/Diploe-BoldItalic.otf",140)
#box_b.color    = Color("Black")
#box_b.db_color = (0,0,0,1)
#box_b.elasticity= gral_elasticity

##------------------------------------------------------

run(simulation_on)