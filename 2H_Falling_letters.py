simulation_on = False
simulation_on = True
##############################
from pyphysicssandbox import *
from pyphysicssandbox import canvas

from importlib import reload

import FS_Tools
reload(FS_Tools)
from FS_Tools import make_fs, add_counter_and_make_fs, fallingParagraph

import drawBot as db

#=================
#General Settings:
#=================
#👉🏼👉🏼Canvas settings:
#-------------------
canvas.window_title = "2H_Falling_LEtters"
canvas.render_width  = 2000
canvas.render_height = 1000
canvas.frames_x_second = 30
canvas.simulation_render_time = 12
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

#### Background
background = cosmetic_box((0, 0), rw, rh)
background.color = Color("Grey")
background.db_color = diploe_grey

#Walls
#left_wall  = static_box((0,0), wall_w, rh)
#right_wall = static_box((rw-wall_w,0), wall_w, rh)
#left_wall.color = wall_color
#right_wall.color = wall_color

#### Floor or ceiling: (both use floorH:int)
if y_limit == "floor":
    floor      = static_box((0, rh-floor_h), rw, floor_h)    
elif y_limit == "ceiling":
    ceiling    = static_box((0, 0), rw, floor_h)
floor.color = floor_color



#### DrawBot

########## FUNCTIONS:
def make_fsLOCAL(string,font_path,font_size,font_variations=None,lineHeight=None):
    f = db.FormattedString()
    f.font(font_path)
    f.fontSize(font_size)
    if font_variations:
        f.fontVariations(**font_variations)
    if not lineHeight:
        lineHeight = font_size*0.90
    f.lineHeight(lineHeight) 
    f+=string
    return f

def add_counter_and_make_fsLOCAL(string,font_path,font_size,font_variations=None,lineHeight=None):
    f = db.FormattedString()
    f.font(font_path)
    f.fontSize(font_size)
    if font_variations:
        f.fontVariations(**font_variations)
    if not lineHeight:
        lineHeight = font_size*0.9
    f.lineHeight(lineHeight) 

    for i, c in enumerate(string):
        f += c
        f.getNSObject().addAttribute_value_range_("char.counter", i, (i, 1))
    return f


def fallingParagraphLOCAL(fs_by_lines, text_box, color_name, font_path, font_size, font_variations=None, line_angle=0):    
    my_shapes = {}    
    if font_variations:
        the_fontVariations = font_variations

    #####Make a rect for every line
    for i, bounds in enumerate(db.textBoxCharacterBounds(fs_by_lines, text_box)):
        x, y, w, h = bounds.bounds 
        print(f"🤪({bounds.bounds}")
        this_baselineOffset = bounds.baselineOffset
        path = db.BezierPath()            
        path.text(bounds.formattedSubString)

        
        add_X = x
        add_Y = y+this_baselineOffset

        if path.bounds():
            minx, miny, maxx, maxy = path.bounds()
        else:
            print("noBounds")

        letter_rect = (add_X, add_Y+ maxy -miny, maxx - minx, maxy- miny)

    ## Simulation Objects make:
        the_string = str(bounds.formattedSubString)
        #print(f"the_string: {the_string}")
        my_shapes[i]= ((letter_rect[0],canvas.win_height-letter_rect[1]),
                        textBox_with_font((letter_rect[0],canvas.win_height-letter_rect[1]),letter_rect[2],letter_rect[3],
                                          the_string,font_path,font_size,font_variations=font_variations))
        my_shapes[i][1].color=Color(color_name)
        my_shapes[i][1].angle=line_angle

    return my_shapes


##########////FUNCTIONS
####------------------

the_font_path = "fonts/VF/DiploeVF.ttf" 
the_font_size = 160
text_color_name = "Black"

text_box_A = (400, 100, 1000, 700)
the_text_A = "Uprootedness is a thing"
the_fontVariations_A ={"wdth":80,"wght":400,"slnt":0}
fs_w_counter_A = add_counter_and_make_fs(the_text_A, the_font_path, the_font_size, font_variations=the_fontVariations_A, lineHeight=the_font_size*1.1)


fallingParagraph(fs_w_counter_A, text_box_A, text_color_name,the_font_path, the_font_size, font_variations=the_fontVariations_A,line_angle=-1)
#fallingParagraph(fs_w_counter_B, text_box_B, text_color_name,the_font_path, the_font_size, font_variations=the_fontVariations_B,line_angle=5)

run(simulation_on)