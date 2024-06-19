simulation_on = False
simulation_on = True
##############################
from pyphysicssandbox import *
from pyphysicssandbox import canvas
import drawBot

#=================
#General Settings:
#=================
#👉🏼👉🏼Canvas settings:
#-------------------
canvas.window_title = "Demo_A_Template"
canvas.render_width  = 2000
canvas.render_height = 1000
canvas.frames_x_second = 30
canvas.simulation_render_time = 10

rw,rh = canvas.render_width, canvas.render_height
w,h = canvas.win_width, canvas.win_height

#----------------------
#Gral physics settings:
#----------------------
canvas.gravity(0,150)  ###👈🏼👈🏼GRAVITY:(x,y)
resistance(.95) #sandbox default is .95
gral_elasticity = .99   #sandbox default is .9
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
y_limit = "floor"
diploe_grey   = rgb_to_normalized(218,219,238,255)
diploe_yellow = rgb_to_normalized(230,228,102,255)
###----------------------------------------
### Physicsiphy world:
left_wall  = static_box((0,0), wall_w, h)
right_wall = static_box((w-wall_w,0), wall_w, h)
left_wall.color = wall_color
right_wall.color = wall_color

#### Floor or ceiling: (both use floorH:int)
if y_limit == "floor":
    floor      = static_box((0, rh-floor_h), rw, floor_h)    
elif y_limit == "ceiling":
    ceiling    = static_box((0, 0), rw, floor_h)
floor.color = floor_color

#### Background
background = cosmetic_box((0, 0), rw, rh)
background.color = Color("Grey")
background.db_color = diploe_grey

#### DrawBot Setup:
####------------------


##------------------------------------------------------


## Simulation Objects setup:
##--------------------------
'''
Setup sandbox objects here.----
'''
boxA=(100,-600,1500,220)
box_a = textBox_with_font((boxA[0], boxA[1]),boxA[2],boxA[3],"HOLA","fonts/Diploe-BoldItalic.otf",140)
box_a.color    = Color("Yellow")
box_a.db_color = diploe_yellow
box_a.elasticity= gral_elasticity

boxB=(200,-300,1000,220)
box_b = textBox_with_font((boxB[0], boxB[1]),boxB[2],boxB[3],"my text","fonts/Diploe-BoldItalic.otf",140)
box_b.color    = Color("Yellow")
box_b.db_color = diploe_yellow
box_b.elasticity= gral_elasticity

##------------------------------------------------------

run(simulation_on)