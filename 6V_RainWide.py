simulation_on = False
simulation_on = True
##############################
from pyphysicssandbox import *
from pyphysicssandbox import canvas
from random import randint

from FS_Tools import make_fs, add_counter_and_make_fs, fallingParagraph
import drawBot as db

#=================
#General Settings:
#=================
#👉🏼👉🏼Canvas settings:
#-------------------
canvas.window_title = "6V_Rain-WideBlack"
canvas.render_width  = 1080
canvas.render_height = 1920
canvas.frames_x_second = 30
canvas.simulation_render_time = 10
#Default canvas color:
canvas.color("Green")

rw,rh = canvas.render_width, canvas.render_height
w,h = canvas.win_width, canvas.win_height

#----------------------
#Gral physics settings:

#----------------------
canvas.gravity(-16,400)  ###👈🏼👈🏼GRAVITY:(x,y)
canvas.resistance(.95) #sandbox default is .95
gral_elasticity = .9   #sandbox default is .9
gral_friction   = .6   #sandbox default is .6
#categories
cat1 = 0b100
cat2 = 0b010
cat3 = 0b001
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
floor_h = 200
floor_color = Color("Red")
wall_w =  200
wall_color = Color("Blue")
y_limit = "floor"

###🎨 COLOR SWATCHES: 🎨
diploe_grey   = rgb_to_normalized(218,219,238,255)
diploe_yellow = rgb_to_normalized(230,228,102,255)
diploe_black  = rgb_to_normalized(0,0,0,255)
####----------------------------------------

#### Background
background = cosmetic_box((0, 0), rw, rh)
background.color = Color("Black")
#background.db_color = diploe_grey

### Physicsiphy world:
#left_wall  = static_box((-wall_w,0), wall_w, rh)
#right_wall = static_box((rw,0), wall_w, rh)
#left_wall.color  = wall_color
#right_wall.color = wall_color

#### Floor or ceiling: (both use floorH:int)
if y_limit == "floor":
    floor      = static_box((-rw/2, rh), rw*2, floor_h)    
elif y_limit == "ceiling":
    ceiling    = static_box((0, 0-rh), rw, floor_h)

floor.color = floor_color
floor.category = cat1



#### DrawBot

########## FUNCTIONS:

def make_fslocal(string,font_path,font_size,font_variations=None,lineHeight=None):
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

def add_counter_and_make_fslocal(string,font_path,font_size,font_variations=None,lineHeight=None):
    f = db.FormattedString()
    f.font(font_path)
    f.fontSize(font_size)
    f.tracking(-1.25)
    if font_variations: 
        f.fontVariations(**font_variations)
    if not lineHeight:
        lineHeight = font_size*0.9
    f.lineHeight(lineHeight) 

    for i, c in enumerate(string):
        f += c
        f.getNSObject().addAttribute_value_range_("char.counter", i, (i, 1))
    return f

def fallingParagraphlocal(fs_by_lines, text_box, color_name, font_path, font_size, font_variations=None, line_angle=0, keep_first_height=False,category=cat1,gravity=None):
    my_shapes = {}   
    

    #####Make a rect for every line
    #print(f"🤓text_box-orig:{text_box}")
    text_box = (text_box[0],canvas.render_height-text_box[1]-text_box[3], text_box[2],text_box[3])#👈🏼convert pysics coords TO drawBot COORDS
    for i, bounds in enumerate(db.textBoxCharacterBounds(fs_by_lines, text_box)):
        x, y, w, h = bounds.bounds #👈🏼drawBot coords
        #print(f"🤓text_box-new:{text_box}")
        #print(f"😎{bounds.bounds}")
        add_y = y+h#👈🏼add height to Y because pyhsics draws from the other side
        letter_rect = (x,add_y,w,h)

    ## Simulation Objects make:
        the_string = str(bounds.formattedSubString)
        #print(f"the_string: {the_string}")
        #print(f"y: {y}")
        #print(f"👹👹canvas.render_height: {canvas.render_height}")

        new_y = canvas.render_height-letter_rect[1]#👈🏼convert drawBot coords TO PHYSICS COORDS
        new_p = (letter_rect[0],new_y)
        #new_y = y
        #print(f"🦋 {new_y}")
        my_shapes[i]= (new_p,
                        textBox_with_font(new_p,letter_rect[2],letter_rect[3],
                                          the_string,font_path,font_size,font_variations=font_variations))
        my_shapes[i][1].color=Color(color_name)
        my_shapes[i][1].angle=line_angle
        my_shapes[i][1].category=category
        if gravity:
            #print("GRAVITY!!!")
            my_shapes[i][1].gravity=gravity
    return my_shapes


##########////FUNCTIONS
####------------------

the_font_path = "fonts/VF/DiploeVF.ttf" 
the_font_size = 160
text_color_name_B = (218,219,238,255) #diploeGrey
#text_color_name_B = (230,228,102,255) #diploeYellow
the_fontVariations_B ={"wdth":150,"wght":700,"slnt":0}
rain_text = "Diplöe "
fs_w_counter_B = add_counter_and_make_fslocal(rain_text*300, the_font_path, the_font_size, font_variations=the_fontVariations_B, lineHeight=the_font_size)
text_box_B = (-50, -3200, rw*1.5, 3800)

floor_margin = 600
floor_he = 100
rain_clearance = 100
cat2_floor = static_box((0-floor_margin, rh+rain_clearance+floor_he), rw+(2*floor_margin),floor_he)
cat2_floor.category=cat2
cat2_floor.elasticity=.95
fallingParagraphlocal(fs_w_counter_B, text_box_B, text_color_name_B,the_font_path, the_font_size, font_variations=the_fontVariations_B,line_angle=randint(-5,10),category=cat2)


run(simulation_on)
