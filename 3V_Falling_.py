simulation_on = False
simulation_on = True
##############################
from pyphysicssandbox import *
from pyphysicssandbox import canvas

from FS_Tools import make_fs, add_counter_and_make_fs, fallingParagraph
import drawBot as db

#=================
#General Settings:
#=================
#👉🏼👉🏼Canvas settings:
#-------------------
canvas.window_title = "3V_Falling_A"
canvas.render_width  = 1080
canvas.render_height = 1920
canvas.frames_x_second = 60
canvas.simulation_render_time = 10
#Default canvas color:
canvas.color("Green")

rw,rh = canvas.render_width, canvas.render_height
w,h = canvas.win_width, canvas.win_height

#----------------------
#Gral physics settings:
#----------------------
gral_gravity=1,50
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
    ceiling    = static_box((0, 0), rw, floor_h)
    ceiling.category = cat2
floor.color   = floor_color

#### Background
background = cosmetic_box((0, 0), rw, rh)
background.color = Color("Yellow")
background.db_color = diploe_yellow

#### DrawBot

########## FUNCTIONS:
def make_fs(string,font_path,font_size,font_variations=None,lineHeight=None):
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

def add_counter_and_make_fs(string,font_path,font_size,font_variations=None,lineHeight=None):
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


def fallingParagraph(fs_by_lines, text_box, color_name, font_path, font_size, font_variations=None, line_angle=0):    
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

font_path = "fonts/VF/DiploeVF.ttf" 
font_size = 200
text_color = (218,219,238,255)
text_box   = (60, 1600, 800, 700)
the_text = "DIPLÖE"
fontVariations = {"wdth":80,"wght":800,"slnt":0}

def physParagraph(font_path, font_size, text_color,text_box, the_text, fontVariations, split_by_glyphs=False):
    text_color_name = text_color
    the_font_path = font_path
    the_font_size = font_size

    text_box_A = text_box
    the_text_A = the_text
    the_fontVariations_A = fontVariations

    if split_by_glyphs:        
        fs_w_counter_A = add_counter_and_make_fs(the_text_A, the_font_path, the_font_size, font_variations=the_fontVariations_A, lineHeight=the_font_size*1.1)
    else:
        fs_w_counter_A = make_fs(the_text_A, the_font_path, the_font_size, font_variations=the_fontVariations_A, lineHeight=the_font_size*1.1)

    return fallingParagraph(fs_w_counter_A, text_box_A, text_color_name, the_font_path, the_font_size, font_variations=the_fontVariations_A,line_angle=-1)


the_boxes = [
    (60, 1600, 800, 700),
    (60, 1400, 800, 700),
    (60, 1200, 800, 700),
    (60, 1000, 800, 700),
    (60, 800, 800, 700),
    (60, 600, 800, 700),
]

for box in the_boxes:
    shapes_dict = physParagraph(font_path, font_size, text_color, box, the_text, fontVariations)
    shapes_dict[0][1].hit((-1000000,0),(400,350))
    
    for dict_entry in shapes_dict:
        print(shapes_dict[dict_entry])
        shapes_dict[dict_entry][1].category= cat1

the_boxes_2 = [
    (400, 000, 800, 700),
    (400, 200, 800, 700),
    (400, 400, 800, 700),
    (400, 600, 800, 700),
    (400, 800, 800, 700),
    (400, 1000, 800, 700),
]

text_color = "Black"
fontVariations = {"wdth":80,"wght":200,"slnt":-11}

for box in the_boxes_2:
    shapes_dict = physParagraph(font_path, font_size, text_color, box, the_text, fontVariations)
    shapes_dict[0][1].hit((1000000,0),(400,350))
    
    for dict_entry in shapes_dict:
        print(shapes_dict[dict_entry])
        shapes_dict[dict_entry][1].category=cat2
        shapes_dict[dict_entry][1].gravity=(gral_gravity[0],-gral_gravity[1])

run(simulation_on)