simulation_on = False
simulation_on = True
##############################
#from importlib import reload

#import FS_Tools
#reload(FS_Tools)
from FS_Tools import make_fs, add_counter_and_make_fs, fallingParagraph

from pyphysicssandbox import *
from pyphysicssandbox import canvas

#=================
#General Settings:
#=================
#👉🏼👉🏼Canvas settings:
#-------------------
canvas.window_title = "1H_Falling_Paragraphs_02"
canvas.render_width  = 2000
canvas.render_height = 1000
canvas.frames_x_second = 30
canvas.simulation_render_time = 15
#Default canvas color:
canvas.color("Green")

rw,rh = canvas.render_width, canvas.render_height
w,h = canvas.win_width, canvas.win_height

#----------------------
#Gral physics settings:
#----------------------
canvas.gravity(-15,400)  ###👈🏼👈🏼GRAVITY:(x,y)
canvas.resistance(.95) #sandbox default is .95
gral_elasticity = .9   #sandbox default is .9
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

###🎨 COLOR SWATCHES: 🎨
diploe_grey   = rgb_to_normalized(218,219,238,255)
diploe_yellow = rgb_to_normalized(230,228,102,255)
diploe_black  = rgb_to_normalized(230,228,102,255)
####----------------------------------------

### Physicsiphy world:
left_wall  = static_box((0,0), wall_w, rh)
right_wall = static_box((rw-wall_w,0), wall_w, rh)
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


#### DrawBot

####------------------

the_font_path = "fonts/VF/DiploeVF.ttf" 
the_font_size = 42
text_color_name = "Black"

text_box_A = (1000, 0, 1000, 500)
the_text_A = "To be rooted is perhaps the most important and least recognized need of the human soul. It is one of the hardest to define. A human being has roots by virtue of his real, active and natural participation in the life of a community which preserves in living shape certain particular treasures of the past and certain particular expectations for the future. This participation is a natural one, in the sense that it is automatically brought about by place, conditions of birth, profession and social surroundings. Every human being needs to have multiple roots. It is necessary for him to draw wellnigh the whole of his moral, intellectual and spiritual life by way of the environment of which he forms a natural part."
the_text_A = the_text_A*2
the_fontVariations_A ={"wdth":80,"wght":400,"slnt":0}
fs_w_counter_A = make_fs(the_text_A, the_font_path, the_font_size, font_variations=the_fontVariations_A, lineHeight=the_font_size*1.1)


text_box_B = (120, 1600, 500, 700)
the_text_B = "To be rooted is perhaps the most important and least recognized need of the human soul. It is one of the hardest to define. A human being has roots by virtue of his real, active and natural participation in the life of a community which preserves in living shape certain particular treasures of the past and certain particular expectations for the future. This participation is a natural one, in the sense that it is automatically brought about by place, conditions of birth, profession and social surroundings. Every human being needs to have multiple roots. It is necessary for him to draw wellnigh the whole of his moral, intellectual and spiritual life by way of the environment of which he forms a natural part."
the_text_B = the_text_B+the_text_B
the_fontVariations_B ={"wdth":30,"wght":200,"slnt":-11}
fs_w_counter_B = make_fs(the_text_B, the_font_path, the_font_size, font_variations=the_fontVariations_B, lineHeight=the_font_size*1.1)

fallingParagraph(fs_w_counter_A, text_box_A, text_color_name,the_font_path, the_font_size, font_variations=the_fontVariations_A,line_angle=0,keep_first_height=True)
#fallingParagraph(fs_w_counter_B, text_box_B, text_color_name,the_font_path, the_font_size, font_variations=the_fontVariations_B,line_angle=5)

run(simulation_on)