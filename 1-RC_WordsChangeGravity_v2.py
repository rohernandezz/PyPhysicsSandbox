#simulation_on = False
simulation_on = True
##############################
from pyphysicssandbox import *
from pyphysicssandbox import canvas
from random import randrange, seed

#from FS_Tools import make_fs, add_counter_and_make_fs, fallingParagraph
#import drawBot as db

#=================
#General Settings:
#=================
#👉🏼👉🏼Canvas settings:
#-------------------
canvas.window_title = "changeGravity02"
canvas.render_width  = 2000
canvas.render_height = 1000
canvas.frames_x_second = 60
canvas.simulation_render_time = 8
seed = 4
#Default canvas color:
canvas.color("Green")

rw,rh = canvas.render_width, canvas.render_height
w,h = canvas.win_width, canvas.win_height

#----------------------
#Gral physics settings:

#----------------------
gravity_values = (80,-200)
canvas.gravity(gravity_values[0], gravity_values[1])  ###👈🏼👈🏼GRAVITY:(x,y)
canvas.resistance(.95) #sandbox default is .95
gral_elasticity = .9 #sandbox default is .9
gral_friction   = .69  #sandbox default is .6
#categories
cat1 = 0b100
cat2 = 0b010
cat3 = 0b001
#------------------------


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
floor_h = 20
floor_color = Color("Red")
wall_w =  5
wall_color = Color("Blue")
y_limit = "both"
diploe_grey   = rgb_to_normalized(218,219,238,255)
diploe_yellow = rgb_to_normalized(230,228,102,255)
###----------------------------------------
### Physicsiphy world:
marginWall=400
left_wall  = static_box((-marginWall,0), wall_w, h)
right_wall = static_box((rw+wall_w+marginWall*1.2,0), wall_w, h)
left_wall.color = wall_color
right_wall.color = wall_color

#### Floor or ceiling: (both use floorH:int)
if y_limit == "floor":
    floor      = static_box((0, rh), rw, floor_h)    
    floor.color = floor_color
if y_limit == "ceiling":
    ceiling    = static_box((0, 0-rh), rw, floor_h)
    ceiling.color = floor_color
if y_limit == "both":
    floor      = static_box((0, rh), rw*2, floor_h)    
    ceiling_clearance=150
    ceiling    = static_box((0, 0-floor_h-ceiling_clearance), rw, floor_h)
    #floor.color = floor_color
    #ceiling.color = floor_color

#### Background
#background = cosmetic_box((0, 0), w, h)
#background.color = Color("Yellow")
#background.db_color = diploe_yellow

#### DrawBot

####------------------


##------------------------------------------------------


## Simulation Objects setup:
##--------------------------
'''
Setup sandbox objects here.----
'''


origins_a = [
            (-100,600),
            (600,800),
            (-270,100),
            (800,350),
            (1340,500),
            (1100,100),
            (-400,800),
            (-10,420),
             ]

texts_a   = [ 
            ("Breaking News","Black"),
            ("Sidebar","Black"),
            ("Continuum","Grey"),
            ("Latitude","Black"),
            ("Diffusion","Grey"),
            ("Longitude","Black"),
            ("Pitch","Grey"),
            ("Grade","Grey"),
            ]

dimensions_a   = [
            (1500, 150),
            (800, 150),
            (1100, 150),
            (860, 150),
            (1020, 150),
            (1000, 150),
            (600, 150),
            (600, 150),
             ]

boxes_a = {}

for i,origin in enumerate(origins_a):
    the_text = texts_a[i]
    the_text_string = the_text[0]
    the_text_color= the_text[1]
    box_dimensions =dimensions_a[i]

    the_font = "fonts/Diploe-BoldItalic.otf"
    if the_text_color == "Grey":
        the_font = "fonts/Diploe-Bold.otf"

    boxes_a[i] = textBox_with_font(origin,box_dimensions[0],box_dimensions[1],the_text_string,the_font,240)
    boxes_a[i].color    = Color(the_text_color)

    if the_text_color == "Grey":
        boxes_a[i].db_color = diploe_grey
    if the_text_color == "Yellow":
        boxes_a[i].db_color = diploe_yellow

    boxes_a[i].elasticity= gral_elasticity
    boxes_a[i].friction=gral_friction
    boxes_a[i].hit((3200000*randrange(-1,1),500000*randrange(-1,1)),(origin[0]+box_dimensions[0]/2,origin[1]-box_dimensions[1]/2))
print(boxes_a)    


def gravity_change_observer(keys):
    #print(f"{gravity}")
    curr_space = boxes_a[i].space
    curr_gravity = curr_space.gravity
    set_grav_x = curr_gravity[0]+1
    set_grav_y = curr_gravity[1]+1
    
    if set_grav_x > 150:
        set_grav_y = curr_gravity[1]+18

    canvas.gravity(set_grav_x,set_grav_y)
    print(f"grav:{curr_gravity}")

def gravity_shift(keys):
    curr_space = boxes_a[i].space
    curr_gravity = curr_space.gravity

    set_grav_x = curr_gravity[0]
    set_grav_y = curr_gravity[1]    
    
    if curr_gravity[0] > 180:
        set_grav_x = curr_gravity[0]-curr_gravity[0]*.75
        set_grav_y = curr_gravity[1]

    canvas.gravity(set_grav_x,set_grav_y)

canvas.add_observer(gravity_change_observer)
#add_observer(gravity_shift)

#boxB=(w*.1,400,w*.8,220)
#box_b = textBox_with_font((boxB[0], boxB[1]),boxB[2],boxB[3],"my text","fonts/Diploe-BoldItalic.otf",140)
#box_b.color    = Color("Black")
#box_b.db_color = (0,0,0,1)
#box_b.elasticity= gral_elasticity

##------------------------------------------------------

run(simulation_on)