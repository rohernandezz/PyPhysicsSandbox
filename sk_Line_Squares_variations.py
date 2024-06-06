simulation_on = False
simulation_on = True
##############################
import drawBot as db
from pyphysicssandbox import *
from random import random, choice

########## FUNCTIONS:
def add_counter_and_make_fs(string,font_path,font_size,fontVariations=None,lineHeight=None):
    f = db.FormattedString()
    f.font(font_path)
    f.fontSize(font_size)
    if fontVariations:
        f.fontVariations(**fontVariations)
    if not lineHeight:
        lineHeight = font_size*0.85
    f.lineHeight(lineHeight) 

    for i, c in enumerate(myText):
        f += c
        f.getNSObject().addAttribute_value_range_("char.counter", i, (i, 1))
    return f


def make_fs(string,font_path,font_size,fontVariations=None,lineHeight=None):
    f = db.FormattedString()
    f.font(font_path)
    f.fontSize(font_size)
    if fontVariations:
        f.fontVariations(**fontVariations)
    if not lineHeight:
        lineHeight = font_size*0.85
    f.lineHeight(lineHeight) 
    f+=string
    return f
##########

#----------------
#General Settings:
#----------------
win_width = 1080
win_height = 1000
w,h = win_width, win_height
window('Falling_Diploe_01', w, h, fps=30)
#-----------------------------
gravity(0,500)       ###👈🏼👈🏼GRAVITY
resistance = .98     #sandbox default is .95
gral_elasticity = .9 #sandbox default is .9
gral_friction   = .6   #sandbox default is .6
#---------------------------------------------------

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

### Physicsiphy world:
left_wall  = static_box((0,0), wall_w, h)
right_wall = static_box((w-wall_w,0), wall_w, h)
left_wall.color = wall_color
right_wall.color = wall_color

#### Floor or ceiling: (both use floorH:int)
if y_limit == "floor":
    floor      = static_box((0, h-floor_h), w, floor_h)    
elif y_limit == "ceiling":
    floor    = static_box((0, 0), w, floor_h)
floor.color = floor_color
floor.elasticity = .9

#### Background
background = cosmetic_box((0, 0), w, h)
background.color = Color("Grey")
background.db_color = (1,0,0,1)

#### DrawBot
text_box = (100, 500, 800, 500)
myText = "Diplöe is a font that is in a bigger paragraph to test how three lines or more work why line 3 dissapears?"
the_font_path = "fonts/VF/DiploeVF.ttf"
the_font_size = 100
#db.font(the_font_path)
#db.fontSize(the_font_size)
#db.lineHeight(the_font_size*.85) 
#fs_w_counter = add_counter_and_make_fs(myText,the_font_path,the_font_size,fontVariations={"wdth":60})
fs_w_counter =                  make_fs(myText,the_font_path,the_font_size,fontVariations={"wdth":60})
my_shapes = {}

#####Make a rect for every character
for i, bounds in enumerate(db.textBoxCharacterBounds(fs_w_counter, text_box)):
    #db.fill(random(), random(), random(), .5)
    x, y, w, h = bounds.bounds 
    #y = win_height-y
    this_baselineOffset = bounds.baselineOffset
    #rect(x, y, w, h)  
    path = db.BezierPath()            
    path.text(bounds.formattedSubString)
    if path.bounds():
        _x, _y, _w, _h = path.bounds()
    else:
        _x, _y, _w, _h = 0,0,0,0

    if 1==1:
        add_X = x
        add_Y = y
        #    db.translate(x, y + bounds.baselineOffset
        #    db.drawPath(path)
        #    db.fill(None)
        #    db.stroke(random(), random(), random(), .5)
        if path.bounds()== None:
            minx, miny, maxx, maxy = 0,0,1,1
        else:   
            minx, miny, maxx, maxy = path.bounds()
        

        letter_rect = (add_X, add_Y + maxy-_y, maxx - minx, maxy- miny)
        db.rect(*letter_rect)
        

        the_string = str(bounds.formattedSubString)
        print(f"the_string: {the_string}")

        my_shapes[i]= ((letter_rect[0],win_height-letter_rect[1]),
                        textBox_with_font((letter_rect[0],win_height-letter_rect[1]),letter_rect[2],letter_rect[3],the_string,the_font_path,the_font_size))
        my_shapes[i][1].body.center_of_mass=(100,0)
    
    #else:
    #    my_shapes[i]= ((letter_rect[0],letter_rect[1]), box((letter_rect[0], letter_rect[1]),letter_rect[2], letter_rect[3]))
    #    my_shapes[i][1].elasticity=0.1
    #    my_shapes[i][1].color=Color("White")
    #    my_shapes[i][1].db_color= (None,None,None,None)
        
    # if i > 0:
    #     prevShape = my_shapes[i-1]
    #     thisShape = my_shapes[i]
    #     print(thisShape[1],prevShape[1])
    #     spring(prevShape[0], prevShape[1], thisShape[0], thisShape[1], thisShape[0][0]-prevShape[0][0]*1.2, 1000, 500)        

####------------------

run(simulation_on) 