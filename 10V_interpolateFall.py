simulation_on = False
simulation_on = True
##############################
from pyphysicssandbox import *
from pyphysicssandbox import canvas
from gridListMaker import divide_in
from random import randint, seed
from FS_Tools import make_fs, add_counter_and_make_fs, fallingParagraph
import drawBot as db

#=================
#General Settings:
#=================
#👉🏼👉🏼Canvas settings:
#-------------------
canvas.window_title = "2Designspaces"
canvas.render_width  = 1080
canvas.render_height = 1920
canvas.frames_x_second = 30
canvas.simulation_render_time = 15
#Default canvas color:
canvas.color("Green")

rw,rh = canvas.render_width, canvas.render_height
w,h = canvas.win_width, canvas.win_height

#----------------------
#Gral physics settings:
#----------------------
gral_gravity=0,200
canvas.gravity(*gral_gravity)  ###👈🏼👈🏼GRAVITY:(x,y)
canvas.resistance(.95) #sandbox default is .95
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
y_limit = "both"

###🎨 COLOR SWATCHES: 🎨
diploe_grey   = rgb_to_normalized(218,219,238,255)
diploe_yellow = rgb_to_normalized(230,228,102,255)
diploe_black  = rgb_to_normalized(230,228,102,255)
####----------------------------------------

### Physicsiphy world:
#categories
cat1 = 0b100
cat2 = 0b010
cat3 = 0b001

left_wall  = static_box((0,0), wall_w, rh)
right_wall = static_box((rw-wall_w,0), wall_w, rh)
left_wall.color = wall_color
right_wall.color = wall_color

#### Floor or ceiling: (both use floorH:int)
if y_limit == "floor":
    floor      = static_box((0, rh-floor_h), rw, floor_h)    
elif y_limit == "ceiling":
    ceiling    = static_box((0, 0), rw, floor_h)
elif y_limit == "both":
    floor      = static_box((0, rh-floor_h), rw, floor_h)    
    ceiling    = static_box((0, 0,floor_h), rw, floor_h)
    #ceiling.category = cat2
    floor.color   = floor_color
    floor.elasticity   = gral_elasticity

#### Background
background = cosmetic_box((0, 0), rw, rh)
background.color = Color("Yellow")
background.db_color = diploe_yellow

the_fontPath  = "fonts/VF/DiploeVF.ttf"
the_font_size = 280
the_text      = "Interpolate"

the_margin = rw/2
box_w = 500
box_h = 300

def thingDo(the_height,the_width): 
    fallingText = textBox_with_font((the_margin,the_height),box_w,300,the_text,the_fontPath,the_font_size,font_variations="Remap")
    fallingText.color = Color("Black")
    fallingText.elasticity = gral_elasticity

for the_height in [200,700,1200]:
    thingDo(the_height,200)
#fallingText2 = textBox_with_font((the_margin,500),box_w,300,the_text,the_fontPath,the_font_size,font_variations="Remap")
#fallingText2.color = Color("Black")
#fallingText.hit((0,-1000000),(0,0))
#fallingText.db_color = diploe_yellow



run(simulation_on)