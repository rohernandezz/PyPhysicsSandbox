#simulation_on = False
simulation_on = True
##############################
from pyphysicssandbox import *
import drawBot

#----------------
#General Settings:
#----------------
win_width = 1080
win_height = 1920
w,h = win_width, win_height
window('DEMO_0', w, h, fps=30)
#-----------------------------
gravity(0,300)       ###👈🏼👈🏼GRAVITY
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
y_limit = "floor"
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
floor.color = floor_color

#### DrawBot

####------------------


##------------------------------------------------------


## Simulation Objects setup:
##--------------------------
'''
Setup sandbox objects here.----
'''
boxA=(w*.1,0,w*.8,220)
box_a = textBox_with_font((boxA[0], boxA[1]),boxA[2],boxA[3],"my text","fonts/Diploe-BoldItalic.otf",140)
box_a.color    = Color("Yellow")
box_a.db_color = diploe_yellow
box_a.elasticity= gral_elasticity

boxB=(w*.1,400,w*.8,220)
box_b = textBox_with_font((boxB[0], boxB[1]),boxB[2],boxB[3],"my text","fonts/Diploe-BoldItalic.otf",140)
box_b.color    = Color("Black")
box_b.db_color = (0,0,0,1)
box_b.elasticity= gral_elasticity

##------------------------------------------------------

run(simulation_on)