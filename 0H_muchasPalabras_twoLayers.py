simulation_on = False
simulation_on = True
##############################
from pyphysicssandbox import *
from pyphysicssandbox import canvas
import drawBot
#import pymunk

#=================
#General Settings:
#=================
#👉🏼👉🏼Canvas settings:
#-------------------
canvas.window_title = "0H_MuchasPalabras_twoLayers"
canvas.render_width  = 2000
canvas.render_height = 1000
canvas.frames_x_second = 30
canvas.simulation_render_time = 20 #10/30 #👈🏼10 frames
#Default canvas color:
canvas.color("Green")

rw,rh = canvas.render_width, canvas.render_height
w,h = canvas.win_width, canvas.win_height

#----------------------
#Gral physics settings:
#----------------------
gral_gravity=(20,400)
canvas.gravity(*gral_gravity)  ###👈🏼👈🏼GRAVITY:(x,y)
canvas.resistance(.99) #sandbox default is .95
gral_elasticity = .9   #sandbox default is .9
gral_friction   = .5   #sandbox default is .6
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
diploe_black  = rgb_to_normalized(0,0,0,255)
####----------------------------------------

### Physicsiphy world:
#categories
cat1 = 0b100
cat2 = 0b010
cat3 = 0b001

###Walls:
#left_wall  = static_box((0,0), wall_w, h)
right_wall = static_box((w-1000,h), wall_w, -h+700)
#left_wall.color = wall_color
right_wall.color = wall_color

#### Floor or ceiling: (both use floorH:int)
if y_limit == "floor":
    floor      = static_box((0, rh-floor_h), rw, floor_h)    
elif y_limit == "ceiling":
    ceiling    = static_box((0, 0), rw, floor_h)
elif y_limit == "both":
    floor      = static_box((0, rh-floor_h), rw, floor_h)    
    ceiling    = static_box((0, 0), rw, floor_h)
    ceiling.category = 0b100
floor.color   = floor_color


#### Background
background = cosmetic_box((0, 0), rw, rh)
background.color = Color("Yellow")
background.db_color = diploe_yellow

#### DrawBot

####------------------


##------------------------------------------------------


## Simulation Objects setup:
##--------------------------
##--------------------------

the_font_size = 160
the_height = 170

'''
Setup sandbox objects here.----
'''
####AMARILLO, BOLDS:
yellow_bold_font_size = the_font_size
yellow_bold_box_height = 180
#TOP LEFT TO BOTTOM RIGHT, roughly by columns:
#boxA=(100,50,1100,yellow_bold_box_height)
#textA = "Liberación"
#box_a = textBox_with_font((boxA[0],boxA[1]), boxA[2],boxA[3], textA, "fonts/DiploeWide-MediumItalic.otf", yellow_bold_font_size)
#box_a.angle    = 2
#box_a.color    = Color("Yellow")
#box_a.db_color = diploe_yellow
#box_a.elasticity= gral_elasticity
#box_a.category=cat2

boxB=(-200,10,1400,yellow_bold_box_height)
textB = "Schockierend"
box_b = textBox_with_font((boxB[0],boxB[1]), boxB[2],boxB[3], textB, "fonts/DiploeWide-SemiboldItalic.otf", yellow_bold_font_size)
box_b.angle    = 6
box_b.color    = Color("Grey")
box_b.db_color = diploe_grey
box_b.elasticity= gral_elasticity
box_b.category=cat2

boxC=(100,280,1050,yellow_bold_box_height)
textC = "Liberación"
box_c = textBox_with_font((boxC[0],boxC[1]), boxC[2],boxC[3], textC, "fonts/DiploeWide-BlackItalic.otf", yellow_bold_font_size)
box_c.angle    = -3
box_c.color    = Color("Grey")
box_c.db_color = diploe_grey
box_c.elasticity= gral_elasticity
box_c.category=cat2

boxD=(1400,-300,1350,yellow_bold_box_height)
textD = "Attonement"
box_d = textBox_with_font((boxD[0],boxD[1]), boxD[2],boxD[3], textD, "fonts/DiploeWide-BoldItalic.otf", yellow_bold_font_size)
box_d.angle    = 5
box_d.color    = Color("Grey")
box_d.db_color = diploe_grey
box_d.elasticity= gral_elasticity
box_d.hit((-30000000,-2000000),(-200,-100))
box_d.category=cat2

box3D=(500,-900,420,yellow_bold_box_height)
text3D = "Mafketel"
box3_d = textBox_with_font((box3D[0],box3D[1]), box3D[2],box3D[3], text3D, "fonts/DiploeNarrow-BoldItalic.otf", yellow_bold_font_size)
box3_d.color    = Color("Grey")
box3_d.db_color = diploe_grey
box3_d.elasticity= gral_elasticity
box3_d.hit((30000000,2000000),(-200,-100))
box3_d.category=cat2



####AMARILLO, BOLDS:
blackcolor_bold_font_size = the_font_size
blackcolor_bold_box_height = the_height
#TOP LEFT TO BOTTOM RIGHT, roughly by columns:

box2A=(200,250,900,blackcolor_bold_box_height)
text2A = "TELEPHOTOGRAPHY"
box2_a = textBox_with_font((box2A[0],box2A[1]), box2A[2],box2A[3], text2A, "fonts/DiploeNarrow-Medium.otf", yellow_bold_font_size)
box2_a.angle    = 3.4
box2_a.color    = Color("Black")
box2_a.db_color = diploe_black
box2_a.elasticity= gral_elasticity
box2_a.category=cat1
box2_a.gravity=(gral_gravity[0],-gral_gravity[1])

box2B=(1550,450,1100,blackcolor_bold_box_height)
text2B = "WALKINGS"
box2_b = textBox_with_font((box2B[0],box2B[1]), box2B[2],box2B[3], text2B, "fonts/DiploeWide-Light.otf", blackcolor_bold_font_size)
box2_b.angle    = -2.3
box2_b.color    = Color("Black")
box2_b.db_color = diploe_black
box2_b.elasticity= gral_elasticity
box2_b.category=cat1
box2_b.gravity=(gral_gravity[0],-gral_gravity[1])

box3B=(960,830,840,blackcolor_bold_box_height)
text3B = "MONOMETALLISTS"
box3_b = textBox_with_font((box3B[0],box3B[1]), box3B[2],box3B[3], text3B, "fonts/DiploeNarrow-Bold.otf", blackcolor_bold_font_size)
box3_b.angle    = -7.3
box3_b.color    = Color("Black")
box3_b.db_color = diploe_black
box3_b.elasticity= gral_elasticity
box3_b.category=cat1
box3_b.gravity=(gral_gravity[0],-gral_gravity[1])
box3_b.hit((-100000,0),(0,0))

box3C=(1000,700,580,blackcolor_bold_box_height)
text3C = "Szempillantás"
box3_c = textBox_with_font((box3C[0],box3C[1]), box3C[2],box3C[3], text3C, "fonts/DiploeNarrow-Light.otf", blackcolor_bold_font_size)
box3_c.angle    = 60
box3_c.color    = Color("Black")
box3_c.db_color = diploe_black
box3_c.elasticity= gral_elasticity
box3_c.hit((-1000,10),(0,0))
box3_c.category=cat1
box3_c.gravity=(gral_gravity[0],-gral_gravity[1])

box4D=(200,600,280,blackcolor_bold_box_height)
text4D = "Polillas"
box4_d = textBox_with_font((box4D[0],box4D[1]), box4D[2],box4D[3], text4D, "fonts/DiploeNarrow-Light.otf", blackcolor_bold_font_size)
box4_d.angle    = 60
box4_d.color    = Color("Black")
box4_d.db_color = diploe_black
box4_d.elasticity= gral_elasticity
box4_d.category=cat1
box4_d.gravity=(gral_gravity[0],-gral_gravity[1])

boxE=(1250,120,830,yellow_bold_box_height)
textE = "Unhabitually"
box_e = textBox_with_font((boxE[0],boxE[1]), boxE[2],boxE[3], textE, "fonts/Diploe-MediumItalic.otf", yellow_bold_font_size)
box_e.angle    = -6
box_e.color    = Color("Black")
box_e.db_color = diploe_black
box_e.elasticity= gral_elasticity
box_e.category=cat1
box_e.gravity=(gral_gravity[0],-gral_gravity[1])
##------------------------------------------------------

run(simulation_on)
